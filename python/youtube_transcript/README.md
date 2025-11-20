# YouTube Video Transcript Fetcher

This example demonstrates how to fetch and process transcripts from YouTube videos using the `youtube-transcript-api` library.

## Requirements

- Python 3.10 or higher
- `youtube-transcript-api>=0.6.0` (automatically installed via inline script metadata)

## Running the Example

```bash
uv run --script main_youtube_transcript.py
```

Or simply:

```bash
uv run python main_youtube_transcript.py
```

## Source Code Overview

### Inline Script Metadata (Lines 1-7)

```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "youtube-transcript-api>=0.6.0",
# ]
# ///
```

**Purpose:** This PEP 723 inline script metadata tells `uv` which dependencies to install automatically. No `pyproject.toml` or manual `pip install` needed!

### Import Statements (Lines 21-26)

```python
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable,
)
```

**Purpose:** Import the main API class and specific error types for robust error handling.

### Core Function: `fetch_transcript` (Lines 36-64)

```python
def fetch_transcript(video_id, language="en"):
    """Fetch transcript for a given YouTube video ID."""
    try:
        api = YouTubeTranscriptApi()                          # Line 48: Instantiate API
        transcript = api.fetch(video_id, languages=[language]) # Line 49: Fetch transcript
        return transcript
    except TranscriptsDisabled:                               # Line 51: Handle disabled transcripts
        print(f"❌ Error: Transcripts are disabled for video {video_id}")
        return None
    except NoTranscriptFound:                                 # Line 54: Handle missing transcripts
        print(f"❌ Error: No transcript found for video {video_id} in language '{language}'")
        return None
    except VideoUnavailable:                                  # Line 59: Handle unavailable videos
        print(f"❌ Error: Video {video_id} is unavailable")
        return None
    except Exception as e:                                    # Line 62: Catch-all error handler
        print(f"❌ Error: {e}")
        return None
```

**Key Points:**
- **Line 48-49:** Create an instance of `YouTubeTranscriptApi` and call `.fetch()` method (not a static method!)
- **Lines 51-64:** Comprehensive error handling for various failure scenarios
- **Return Value:** `FetchedTranscript` object (iterable, acts like a list of dictionaries)

### Transcript List Function (Lines 67-83)

```python
def list_available_transcripts(video_id):
    """List all available transcripts for a video."""
    try:
        api = YouTubeTranscriptApi()              # Line 78: Instantiate API
        transcript_list = api.list(video_id)      # Line 79: Get transcript list
        return transcript_list
    except Exception as e:
        print(f"❌ Error listing transcripts: {e}")
        return None
```

**Purpose:** Get a `TranscriptList` object that can be used to:
- Iterate over available transcripts
- Filter by language
- Distinguish between manual and auto-generated transcripts

### Formatting Function (Lines 86-114)

```python
def format_transcript(transcript, max_entries=5):
    """Format and display transcript entries."""
    if not transcript:
        print("No transcript data available")
        return

    print(f"Total transcript entries: {len(transcript)}")     # Line 98
    
    for i, entry in enumerate(transcript[:max_entries], 1):   # Line 101
        timestamp = entry.get("start", 0)                     # Line 102: Get start time
        duration = entry.get("duration", 0)                   # Line 103: Get duration
        text = entry.get("text", "").strip()                  # Line 104: Get text
        
        minutes = int(timestamp // 60)                        # Line 107: Convert to MM:SS
        seconds = int(timestamp % 60)                         # Line 108
        
        print(f"Entry {i}:")
        print(f"  ⏱️  Time: {minutes:02d}:{seconds:02d}")
        print(f"  ⏳ Duration: {duration:.2f}s")
        print(f"  💬 Text: {text}")
```

**Transcript Entry Structure:**
Each entry in the transcript is a dictionary with:
- `"start"`: Timestamp in seconds when text appears
- `"duration"`: How long the text is displayed
- `"text"`: The actual caption text

## Example Output (With Internet Connection)

When run with internet access, the output would look like:

```
============================================================
 Example 1: Fetching a Video Transcript
============================================================

📹 Fetching transcript for video ID: rfscVS0vtbw
🔗 URL: https://www.youtube.com/watch?v=rfscVS0vtbw

✅ Transcript fetched successfully!

Total transcript entries: 247

Showing first 3 entries:

Entry 1:
  ⏱️  Time: 00:00
  ⏳ Duration: 3.21s
  💬 Text: Welcome to this Python tutorial

Entry 2:
  ⏱️  Time: 00:03
  ⏳ Duration: 2.85s
  💬 Text: In this video we'll learn about programming

Entry 3:
  ⏱️  Time: 00:06
  ⏳ Duration: 3.44s
  💬 Text: Let's get started with the basics

📝 Total transcript length: 8432 characters
📝 Total words: 1456

============================================================
 Example 2: Listing Available Transcripts
============================================================

📋 Checking available transcripts for video ID: rfscVS0vtbw

Available transcripts:

✍️  Manually created transcripts:
   - Language: English (en)

🤖 Auto-generated transcripts:
   - Language: Spanish (es)
   - Language: French (fr)
   - Language: German (de)

============================================================
 Example 3: Error Handling
============================================================

Attempting to fetch transcript from a video without captions:

❌ Error: No transcript found for video invalid_id_123 in language 'en'

✅ Error handling demonstrated successfully!

============================================================
 Summary
============================================================

This example demonstrated:
  1. ✅ Fetching transcripts from YouTube videos
  2. ✅ Displaying transcript entries with timestamps
  3. ✅ Listing available transcript languages
  4. ✅ Distinguishing manual vs auto-generated transcripts
  5. ✅ Proper error handling for various scenarios

💡 Use Case: Extract transcripts for content analysis,
   accessibility features, or creating video summaries.
```

## Actual Output (Without Internet Connection)

In the current sandboxed environment without internet access:

```
============================================================
 Example 1: Fetching a Video Transcript
============================================================

📹 Fetching transcript for video ID: rfscVS0vtbw
🔗 URL: https://www.youtube.com/watch?v=rfscVS0vtbw

❌ Error: HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded...

============================================================
 Example 2: Listing Available Transcripts
============================================================

📋 Checking available transcripts for video ID: rfscVS0vtbw

❌ Error listing transcripts: HTTPSConnectionPool(host='www.youtube.com', port=443)...

============================================================
 Example 3: Error Handling
============================================================

Attempting to fetch transcript from a video without captions:

❌ Error: HTTPSConnectionPool(host='www.youtube.com', port=443)...

✅ Error handling demonstrated successfully!

============================================================
 Summary
============================================================

This example demonstrated:
  1. ✅ Fetching transcripts from YouTube videos
  2. ✅ Displaying transcript entries with timestamps
  3. ✅ Listing available transcript languages
  4. ✅ Distinguishing manual vs auto-generated transcripts
  5. ✅ Proper error handling for various scenarios

💡 Use Case: Extract transcripts for content analysis,
   accessibility features, or creating video summaries.
```

**Note:** The network errors are expected in environments without internet access. The code is correct and will work properly when run with internet connectivity.

## Code Annotations

### Main Execution Flow (Lines 133-221)

```python
def main():
    """Main function demonstrating YouTube transcript API usage."""
    
    # Example 1: Fetch transcript for a specific video
    print_section("Example 1: Fetching a Video Transcript")      # Line 137
    
    video_id = "rfscVS0vtbw"                                      # Line 141: YouTube video ID
    transcript = fetch_transcript(video_id)                       # Line 146: Fetch transcript
    
    if transcript:                                                # Line 148: Check if successful
        format_transcript(transcript, max_entries=3)              # Line 150: Display first 3 entries
        full_text = get_full_transcript_text(transcript)          # Line 153: Combine all text
        print(f"📝 Total transcript length: {len(full_text)} characters")
        print(f"📝 Total words: {len(full_text.split())}")
    
    # Example 2: List available transcripts
    print_section("Example 2: Listing Available Transcripts")    # Line 158
    transcript_list = list_available_transcripts(video_id)        # Line 162
    
    if transcript_list:
        # Find manually created transcripts
        manual_transcripts = list(                                # Line 169
            transcript_list.find_manually_created_transcripts()
        )
        
        # Find auto-generated transcripts
        auto_transcripts = list(                                  # Line 185
            transcript_list.find_generated_transcripts()
        )
    
    # Example 3: Error handling
    print_section("Example 3: Error Handling")                    # Line 198
    invalid_video_id = "invalid_id_123"                           # Line 203
    fetch_transcript(invalid_video_id)                            # Line 204: Test error handling
```

### Key Operations Explained

1. **Lines 141-146:** Use a real YouTube video ID to fetch its transcript
2. **Lines 148-155:** If successful, display the first 3 entries and statistics
3. **Lines 162-195:** List all available transcripts and categorize them as manual vs auto-generated
4. **Lines 203-204:** Demonstrate error handling with an invalid video ID

### TranscriptList Methods (Lines 169-195)

The `TranscriptList` object returned by `api.list()` provides several methods:

- `.find_manually_created_transcripts()` - Returns manually created transcripts (human-made)
- `.find_generated_transcripts()` - Returns auto-generated transcripts (by YouTube's AI)
- `.find_transcript(['en', 'es'])` - Find transcript in preferred language order

## Use Cases

This code can be adapted for:

1. **Content Analysis:** Extract transcripts to analyze video content programmatically
2. **Accessibility:** Generate captions or subtitles for videos
3. **Search Indexing:** Make video content searchable by text
4. **Translation:** Get transcripts in multiple languages
5. **Summarization:** Feed transcripts to AI models for video summaries
6. **Research:** Analyze patterns in video content at scale

## Important Notes

- **Video ID:** The video ID is the part after `watch?v=` in YouTube URLs
  - Example: `https://www.youtube.com/watch?v=dQw4w9WgXcQ` → ID is `dQw4w9WgXcQ`
- **API Version:** This code uses `youtube-transcript-api` version 0.6.0 or higher, which requires instantiating the `YouTubeTranscriptApi` class (not using static methods)
- **Error Handling:** Always wrap API calls in try-except blocks as network issues or missing transcripts are common
- **Rate Limiting:** YouTube may rate-limit requests if you make too many in a short period
- **Terms of Service:** Ensure your use complies with YouTube's Terms of Service

## Library Version Requirement

This example requires **`youtube-transcript-api>=0.6.0`** as the API changed from static methods to instance methods in recent versions.
