"""Manifest loader and parser for courses.yaml"""

import yaml
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, Optional, List


@dataclass
class CourseCapabilities:
    """Course capabilities: what content types it has."""
    videos: bool
    notes: bool
    exercises: bool
    transcripts: bool
    dashboard: bool


@dataclass
class Course:
    """A course in the manifest."""
    id: int
    name: str
    path: str
    capabilities: CourseCapabilities
    processor_script: Optional[str]
    last_processed: str


class Manifest:
    """In-memory representation of courses.yaml."""

    def __init__(self, data: dict):
        self.data = data
        self.courses: List[Course] = []

        for course_id, course_data in data.get('courses', {}).items():
            caps = CourseCapabilities(**course_data['capabilities'])
            course = Course(
                id=int(course_id),
                name=course_data['name'],
                path=course_data['path'],
                capabilities=caps,
                processor_script=course_data.get('processor_script'),
                last_processed=course_data.get('last_processed', '2026-09-22')
            )
            self.courses.append(course)

        # Sort by ID
        self.courses.sort(key=lambda c: c.id)

    def to_table(self) -> str:
        """Return markdown table of courses and their capabilities."""
        lines = [
            "| ID | Name | Videos | Notes | Exercises | Transcripts | Dashboard |",
            "|--|--|--|--|--|--|--|"
        ]
        for c in self.courses:
            videos_mark = '✅' if c.capabilities.videos else '❌'
            notes_mark = '✅' if c.capabilities.notes else '❌'
            ex_mark = '✅' if c.capabilities.exercises else '❌'
            trans_mark = '✅' if c.capabilities.transcripts else '❌'
            dash_mark = '✅' if c.capabilities.dashboard else '❌'

            lines.append(
                f"| {c.id} | {c.name} | {videos_mark} | {notes_mark} | {ex_mark} | {trans_mark} | {dash_mark} |"
            )
        return "\n".join(lines)


def load_manifest(path: str = "courses.yaml") -> Manifest:
    """Load and parse courses.yaml"""
    manifest_path = Path(path)
    if not manifest_path.exists():
        raise FileNotFoundError(f"courses.yaml not found at {path}")

    with open(manifest_path, encoding='utf-8') as f:
        data = yaml.safe_load(f)

    return Manifest(data)
