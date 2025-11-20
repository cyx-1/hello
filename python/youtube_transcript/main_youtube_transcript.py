#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "youtube-transcript-api>=0.6.0",
# ]
# ///

"""
YouTube Transcript Retrieval Example

This script demonstrates how to retrieve transcripts from YouTube videos
using the youtube-transcript-api library.
"""

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable,
)


def print_section_header(title: str) -> None:
    """Print a formatted section header."""
    print(f"\n{'=' * 70}")
    print(f"{title:^70}")
    print(f"{'=' * 70}\n")


def fetch_transcript(video_id: str) -> None:
    """
    Fetch and display the transcript for a given YouTube video ID.

    Args:
        video_id: The YouTube video ID (e.g., 'dQw4w9WgXcQ')
    """
    try:
        # Line 39: Create API instance and fetch the transcript
        print(f"Fetching transcript for video ID: {video_id}")
        api = YouTubeTranscriptApi()
        fetched = api.fetch(video_id)
        transcript_list = fetched.segments

        # Line 44: Display transcript statistics
        print(f"\nTotal segments: {len(transcript_list)}")
        print(f"First segment starts at: {transcript_list[0]['start']:.2f}s")
        print(
            f"Last segment ends at: "
            f"{transcript_list[-1]['start'] + transcript_list[-1]['duration']:.2f}s"
        )

        # Line 52: Display first 5 segments
        print("\nFirst 5 transcript segments:")
        print("-" * 70)
        for i, entry in enumerate(transcript_list[:5], 1):
            timestamp = entry["start"]
            duration = entry["duration"]
            text = entry["text"]
            print(f"{i}. [{timestamp:.2f}s - {timestamp + duration:.2f}s]")
            print(f"   {text}")
            print()

    except TranscriptsDisabled:
        print(f"Error: Transcripts are disabled for video ID: {video_id}")
    except NoTranscriptFound:
        print(f"Error: No transcript found for video ID: {video_id}")
    except VideoUnavailable:
        print(f"Error: Video is unavailable for video ID: {video_id}")
    except Exception as e:
        print(f"Error fetching transcript: {e}")


def fetch_transcript_with_language(video_id: str, language_code: str) -> None:
    """
    Fetch transcript in a specific language.

    Args:
        video_id: The YouTube video ID
        language_code: Language code (e.g., 'en', 'es', 'fr')
    """
    try:
        print(
            f"Fetching transcript for video ID: {video_id} in language: {language_code}"
        )
        api = YouTubeTranscriptApi()
        fetched = api.fetch(video_id, languages=[language_code])
        transcript_list = fetched.segments

        print(f"\nFound {len(transcript_list)} segments in {language_code}")
        print("\nFirst 3 segments:")
        print("-" * 70)
        for i, entry in enumerate(transcript_list[:3], 1):
            print(f"{i}. [{entry['start']:.2f}s] {entry['text']}")

    except NoTranscriptFound:
        print(f"Error: No transcript found in language '{language_code}'")
    except Exception as e:
        print(f"Error: {e}")


def list_available_transcripts(video_id: str) -> None:
    """
    List all available transcripts for a video.

    Args:
        video_id: The YouTube video ID
    """
    try:
        print(f"Listing available transcripts for video ID: {video_id}")
        api = YouTubeTranscriptApi()
        transcript_list = api.list(video_id)

        print("\nManually created transcripts:")
        print("-" * 70)
        for transcript in transcript_list:
            if not transcript.is_generated:
                print(f"  - {transcript.language} ({transcript.language_code})")

        print("\nAuto-generated transcripts:")
        print("-" * 70)
        for transcript in transcript_list:
            if transcript.is_generated:
                print(f"  - {transcript.language} ({transcript.language_code})")

    except Exception as e:
        print(f"Error listing transcripts: {e}")


def main() -> None:
    """Main function to demonstrate YouTube transcript retrieval."""

    print_section_header("YouTube Transcript API Demo")

    # Example 1: Fetch transcript for a popular educational video
    # Using well-known video IDs that have transcripts
    video_id_1 = "jNQXAC9IVRw"  # "Me at the zoo" - first YouTube video
    print_section_header("Example 1: Basic Transcript Retrieval")
    fetch_transcript(video_id_1)

    # Example 2: List available transcripts
    print_section_header("Example 2: List Available Transcripts")
    list_available_transcripts(video_id_1)

    # Example 3: Fetch transcript in specific language (English)
    print_section_header("Example 3: Fetch Transcript in Specific Language")
    fetch_transcript_with_language(video_id_1, "en")

    print_section_header("Demo Complete")
    print("\nKey Points:")
    print("  1. Create an instance of YouTubeTranscriptApi()")
    print("  2. Use api.fetch() to retrieve transcript, access segments via .segments")
    print("  3. Specify languages parameter to get transcript in specific language")
    print("  4. Use api.list() to see all available transcript options")
    print("  5. Each transcript entry contains: text, start time, and duration")
    print("  6. Handle exceptions for disabled/unavailable transcripts")


if __name__ == "__main__":
    main()
