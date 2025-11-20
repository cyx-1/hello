# YouTube Video Transcript Retrieval in Python

This example demonstrates how to retrieve transcripts from YouTube videos using the `youtube-transcript-api` library in Python.

## Overview

The script showcases three main operations:
1. **Basic transcript retrieval** - Fetching and displaying transcript segments
2. **Listing available transcripts** - Discovering all transcript options for a video
3. **Language-specific retrieval** - Fetching transcripts in a specific language

## How to Run

```bash
uv run python/youtube_transcript/main_youtube_transcript.py
```

The script uses inline script metadata (PEP 723) to automatically manage dependencies. No separate `pyproject.toml` or manual pip installation is needed.

## Key Source Code

### API Instance Creation and Transcript Fetching (Lines 39-43)

```python
39→        # Line 39: Create API instance and fetch the transcript
40→        print(f"Fetching transcript for video ID: {video_id}")
41→        api = YouTubeTranscriptApi()
42→        fetched = api.fetch(video_id)
43→        transcript_list = fetched.segments
```

**Explanation:**
- Line 41: Creates an instance of the `YouTubeTranscriptApi` class
- Line 42: Calls `fetch()` method with the video ID to retrieve the transcript
- Line 43: Accesses the `segments` property to get the list of transcript entries

### Processing Transcript Segments (Lines 56-62)

```python
56→        for i, entry in enumerate(transcript_list[:5], 1):
57→            timestamp = entry["start"]
58→            duration = entry["duration"]
59→            text = entry["text"]
60→            print(f"{i}. [{timestamp:.2f}s - {timestamp + duration:.2f}s]")
61→            print(f"   {text}")
```

**Explanation:**
- Line 56: Iterates through the first 5 transcript segments
- Lines 57-59: Each segment is a dictionary containing three key fields:
  - `start`: The timestamp when the text appears (in seconds)
  - `duration`: How long the text is displayed (in seconds)
  - `text`: The actual transcript text
- Lines 60-61: Displays the time range and text for each segment

### Language-Specific Transcript Retrieval (Lines 86-88)

```python
86→        api = YouTubeTranscriptApi()
87→        fetched = api.fetch(video_id, languages=[language_code])
88→        transcript_list = fetched.segments
```

**Explanation:**
- Line 87: The `fetch()` method accepts a `languages` parameter to request a specific language
- Pass a list of language codes (e.g., `['en']` for English, `['es']` for Spanish)

### Listing Available Transcripts (Lines 111-124)

```python
111→        api = YouTubeTranscriptApi()
112→        transcript_list = api.list(video_id)
113→
114→        print("\nManually created transcripts:")
115→        print("-" * 70)
116→        for transcript in transcript_list:
117→            if not transcript.is_generated:
118→                print(f"  - {transcript.language} ({transcript.language_code})")
119→
120→        print("\nAuto-generated transcripts:")
121→        print("-" * 70)
122→        for transcript in transcript_list:
123→            if transcript.is_generated:
124→                print(f"  - {transcript.language} ({transcript.language_code})")
```

**Explanation:**
- Line 112: The `list()` method returns all available transcript options
- Lines 117-118: Filters for manually created (human-written) transcripts
- Lines 123-124: Filters for auto-generated (AI-generated) transcripts
- Each transcript object has `is_generated`, `language`, and `language_code` properties

### Error Handling (Lines 64-71)

```python
64→    except TranscriptsDisabled:
65→        print(f"Error: Transcripts are disabled for video ID: {video_id}")
66→    except NoTranscriptFound:
67→        print(f"Error: No transcript found for video ID: {video_id}")
68→    except VideoUnavailable:
69→        print(f"Error: Video is unavailable for video ID: {video_id}")
70→    except Exception as e:
71→        print(f"Error fetching transcript: {e}")
```

**Explanation:**
- Lines 64-69: Specific exception handling for common transcript-related errors
- Line 70-71: Generic exception handler for unexpected errors (e.g., network issues, API changes)

## Expected Output

### Successful Execution

When the script successfully retrieves a transcript, you would see output like:

```
======================================================================
                Example 1: Basic Transcript Retrieval
======================================================================

Fetching transcript for video ID: jNQXAC9IVRw

Total segments: 12
First segment starts at: 0.00s
Last segment ends at: 18.53s

First 5 transcript segments:
----------------------------------------------------------------------
1. [0.00s - 3.50s]
   All right, so here we are in front of the elephants.

2. [3.50s - 6.20s]
   The cool thing about these guys is that they have really,

3. [6.20s - 8.95s]
   really, really long trunks.

4. [8.95s - 11.10s]
   And that's cool.

5. [11.10s - 13.65s]
   And that's pretty much all there is to say.
```

### When Transcripts Are Unavailable

If YouTube blocks the request or transcripts are not available:

```
======================================================================
                Example 1: Basic Transcript Retrieval
======================================================================

Fetching transcript for video ID: jNQXAC9IVRw
Error fetching transcript:
Could not retrieve a transcript for the video https://www.youtube.com/watch?v=jNQXAC9IVRw!
This is most likely caused by:

Request to YouTube failed: 403 Client Error: Forbidden for url: ...
```

**Note:** YouTube may return 403 Forbidden errors when detecting automated access. This is a known limitation of web scraping approaches. The error demonstrates proper exception handling (Line 70-71).

### Listing Available Transcripts (Success Case)

```
======================================================================
                Example 2: List Available Transcripts
======================================================================

Listing available transcripts for video ID: jNQXAC9IVRw

Manually created transcripts:
----------------------------------------------------------------------
  - English (en)

Auto-generated transcripts:
----------------------------------------------------------------------
  - Spanish (es)
  - French (fr)
  - German (de)
```

## Output-to-Source Code Correlation

1. **"Fetching transcript for video ID:"** → Generated by Line 40
2. **"Total segments: 12"** → Calculated by Line 46 using `len(transcript_list)`
3. **"First segment starts at: 0.00s"** → Retrieved from Line 47 accessing `transcript_list[0]['start']`
4. **Time range "[0.00s - 3.50s]"** → Computed by Lines 57-60 using `start` and `duration` fields
5. **Transcript text** → Extracted by Line 59 from `entry["text"]`
6. **"Manually created transcripts:"** → Printed by Line 114, filtered by Line 117
7. **Error messages** → Generated by exception handlers at Lines 64-71

## Important Notes

### Version Requirements

This code requires:
- **Python 3.8+** (specified in line 3 of inline script metadata)
- **youtube-transcript-api >= 0.6.0** (specified in line 5)

The `youtube-transcript-api` library underwent API changes in version 0.6.0+:
- Old API: `YouTubeTranscriptApi.get_transcript()` (class method)
- New API: `YouTubeTranscriptApi().fetch()` (instance method)

This example uses the newer instance-based API.

### Common Issues

1. **403 Forbidden Errors**: YouTube may block automated transcript requests. This is a limitation of the library's web scraping approach, not a bug in the code.

2. **No Transcript Found**: Not all videos have transcripts available. Videos without captions will raise `NoTranscriptFound`.

3. **TranscriptsDisabled**: Some video owners disable transcripts entirely.

### Practical Applications

This code pattern can be used for:
- Creating subtitle files from YouTube videos
- Analyzing video content programmatically
- Building search indices for video content
- Accessibility tools and caption editors
- Content summarization and analysis

## Key Takeaways

1. **Create an instance**: `api = YouTubeTranscriptApi()` (Line 41)
2. **Fetch transcripts**: `api.fetch(video_id)` returns a `FetchedTranscript` object (Line 42)
3. **Access segments**: Use `.segments` property to get transcript list (Line 43)
4. **Specify language**: Pass `languages=['en']` to `fetch()` for specific languages (Line 87)
5. **List options**: Use `api.list(video_id)` to discover available transcripts (Line 112)
6. **Handle errors**: Always catch `TranscriptsDisabled`, `NoTranscriptFound`, and `VideoUnavailable` (Lines 64-69)
