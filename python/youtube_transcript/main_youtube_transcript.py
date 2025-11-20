#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "youtube-transcript-api>=0.6.0",
# ]
# ///

"""
YouTube Video Transcript Fetcher

This script demonstrates how to use the youtube-transcript-api library
to fetch transcripts from YouTube videos. It showcases:
1. Fetching transcripts by video ID
2. Handling different languages
3. Listing available transcripts
4. Error handling for videos without transcripts
5. Formatting and displaying transcript data
"""

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable,
)


def print_section(title):
    """Print a formatted section header."""
    print(f"\n{'=' * 60}")
    print(f" {title}")
    print(f"{'=' * 60}\n")


def fetch_transcript(video_id, language="en"):
    """
    Fetch transcript for a given YouTube video ID.

    Args:
        video_id: YouTube video ID (e.g., 'dQw4w9WgXcQ')
        language: Language code for transcript (default: 'en')

    Returns:
        List of transcript entries or None if error occurs
    """
    try:
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id, languages=[language])
        return transcript
    except TranscriptsDisabled:
        print(f"❌ Error: Transcripts are disabled for video {video_id}")
        return None
    except NoTranscriptFound:
        print(
            f"❌ Error: No transcript found for video {video_id} in language '{language}'"
        )
        return None
    except VideoUnavailable:
        print(f"❌ Error: Video {video_id} is unavailable")
        return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None


def list_available_transcripts(video_id):
    """
    List all available transcripts for a video.

    Args:
        video_id: YouTube video ID

    Returns:
        TranscriptList object or None if error occurs
    """
    try:
        api = YouTubeTranscriptApi()
        transcript_list = api.list(video_id)
        return transcript_list
    except Exception as e:
        print(f"❌ Error listing transcripts: {e}")
        return None


def format_transcript(transcript, max_entries=5):
    """
    Format and display transcript entries.

    Args:
        transcript: List of transcript entries
        max_entries: Maximum number of entries to display
    """
    if not transcript:
        print("No transcript data available")
        return

    print(f"Total transcript entries: {len(transcript)}")
    print(f"\nShowing first {min(max_entries, len(transcript))} entries:\n")

    for i, entry in enumerate(transcript[:max_entries], 1):
        timestamp = entry.get("start", 0)
        duration = entry.get("duration", 0)
        text = entry.get("text", "").strip()

        # Format timestamp as MM:SS
        minutes = int(timestamp // 60)
        seconds = int(timestamp % 60)

        print(f"Entry {i}:")
        print(f"  ⏱️  Time: {minutes:02d}:{seconds:02d}")
        print(f"  ⏳ Duration: {duration:.2f}s")
        print(f"  💬 Text: {text}")
        print()


def get_full_transcript_text(transcript):
    """
    Combine all transcript entries into a single text.

    Args:
        transcript: List of transcript entries

    Returns:
        Combined text string
    """
    if not transcript:
        return ""

    return " ".join([entry.get("text", "").strip() for entry in transcript])


def main():
    """Main function demonstrating YouTube transcript API usage."""

    # Example 1: Fetch transcript for a specific video
    print_section("Example 1: Fetching a Video Transcript")

    # Using a short YouTube video ID for demonstration
    # This is a public educational video about Python
    video_id = "rfscVS0vtbw"  # "Learn Python - Full Course for Beginners" (short intro)

    print(f"📹 Fetching transcript for video ID: {video_id}")
    print(f"🔗 URL: https://www.youtube.com/watch?v={video_id}\n")

    transcript = fetch_transcript(video_id)

    if transcript:
        print("✅ Transcript fetched successfully!\n")
        format_transcript(transcript, max_entries=3)

        # Get full text
        full_text = get_full_transcript_text(transcript)
        print(f"📝 Total transcript length: {len(full_text)} characters")
        print(f"📝 Total words: {len(full_text.split())}")

    # Example 2: List available transcripts
    print_section("Example 2: Listing Available Transcripts")

    print(f"📋 Checking available transcripts for video ID: {video_id}\n")

    transcript_list = list_available_transcripts(video_id)

    if transcript_list:
        print("Available transcripts:\n")

        # Try to get manually created transcripts
        try:
            manual_transcripts = list(
                transcript_list.find_manually_created_transcripts()
            )
            if manual_transcripts:
                print("✍️  Manually created transcripts:")
                for transcript in manual_transcripts:
                    print(
                        f"   - Language: {transcript.language} ({transcript.language_code})"
                    )
            else:
                print("✍️  No manually created transcripts available")
        except Exception:
            print("✍️  No manually created transcripts available")

        # Try to get auto-generated transcripts
        try:
            auto_transcripts = list(transcript_list.find_generated_transcripts())
            if auto_transcripts:
                print("\n🤖 Auto-generated transcripts:")
                for transcript in auto_transcripts:
                    print(
                        f"   - Language: {transcript.language} ({transcript.language_code})"
                    )
            else:
                print("\n🤖 No auto-generated transcripts available")
        except Exception:
            print("\n🤖 No auto-generated transcripts available")

    # Example 3: Handling errors
    print_section("Example 3: Error Handling")

    print("Attempting to fetch transcript from a video without captions:\n")

    # Using an invalid or caption-disabled video ID
    invalid_video_id = "invalid_id_123"
    fetch_transcript(invalid_video_id)

    print("\n✅ Error handling demonstrated successfully!")

    # Summary
    print_section("Summary")
    print("This example demonstrated:")
    print("  1. ✅ Fetching transcripts from YouTube videos")
    print("  2. ✅ Displaying transcript entries with timestamps")
    print("  3. ✅ Listing available transcript languages")
    print("  4. ✅ Distinguishing manual vs auto-generated transcripts")
    print("  5. ✅ Proper error handling for various scenarios")
    print("\n💡 Use Case: Extract transcripts for content analysis,")
    print("   accessibility features, or creating video summaries.\n")


if __name__ == "__main__":
    main()
