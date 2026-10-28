"""Click CLI for MACI Platform"""

import sys
import click
from pathlib import Path
from maci_platform.manifest import load_manifest

# Force UTF-8 on Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


@click.group()
def main():
    """MACI Platform CLI — unified entry point for course management."""
    pass


@main.command()
@click.option('--course', required=True, help='Course ID: 80014, 80038, ...')
@click.option('--with-videos', is_flag=True, help='Process videos if available')
def process(course, with_videos):
    """Process a course using its configured processor script."""
    try:
        course_id = int(course)
        manifest = load_manifest()

        course_obj = next((c for c in manifest.courses if c.id == course_id), None)
        if not course_obj:
            click.echo(f"❌ Course {course_id} not found in manifest", err=True)
            return 1

        if not course_obj.processor_script:
            click.echo(f"⚠️  Course {course_id} ({course_obj.name}) has no processor script yet", err=True)
            return 1

        click.echo(f"📥 Processing {course_obj.name} ({course_id})...")
        click.echo(f"   Path: {course_obj.path}")
        click.echo(f"   Script: {course_obj.processor_script}")
        click.echo("   ⏳ [Processor invocation to be implemented in FASE-1]")

        return 0
    except ValueError:
        click.echo(f"❌ Invalid course ID: {course}", err=True)
        return 1


@main.command()
def status():
    """Show course processing status as a capability matrix."""
    try:
        manifest = load_manifest()
        click.echo()
        click.echo(manifest.to_table())
        click.echo()
        return 0
    except FileNotFoundError as e:
        click.echo(f"❌ {e}", err=True)
        return 1


@main.command()
def report():
    """Generate capability report (summary + matrix)."""
    try:
        manifest = load_manifest()
        total = len(manifest.courses)
        with_content = sum(
            1 for c in manifest.courses
            if any([
                c.capabilities.videos,
                c.capabilities.notes,
                c.capabilities.exercises,
                c.capabilities.transcripts,
                c.capabilities.dashboard
            ])
        )

        click.echo()
        click.echo("📊 PLATFORM STATUS")
        click.echo(f"   Courses: {total}/6")
        click.echo(f"   With content: {with_content}/{total} ({100*with_content//total}%)")
        click.echo()
        click.echo(manifest.to_table())
        click.echo()
        return 0
    except FileNotFoundError as e:
        click.echo(f"❌ {e}", err=True)
        return 1


if __name__ == '__main__':
    main()
