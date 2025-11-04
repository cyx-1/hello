# Boto3 AWS S3 Example: Comprehensive S3 Operations

This example demonstrates how to use the **boto3** library (AWS SDK for Python) to interact with Amazon S3 (Simple Storage Service). It covers all essential S3 operations including bucket management, object uploads/downloads, metadata handling, and presigned URLs.

## Key Concepts Illustrated

1. **Client vs Resource Interfaces** - Two ways to interact with AWS services
2. **Bucket Operations** - Creating, listing, and deleting buckets
3. **Object Operations** - Uploading, downloading, listing, copying, and deleting objects
4. **Metadata Management** - Working with custom metadata and object properties
5. **Presigned URLs** - Generating temporary URLs for secure access

## Requirements

- **Python Version**: Python 3.8 or higher
- **Dependencies**:
  - `boto3>=1.34.0` - AWS SDK for Python
  - `moto[s3]>=5.0.0` - AWS service mocking library

**Note**: This example uses `moto` to mock AWS S3, allowing it to run without actual AWS credentials or incurring costs.

## Running the Example

```bash
uv run python main_aws_s3.py
```

## Source Code and Output Analysis

### 1. Client vs Resource Interfaces

**Source Code (main_aws_s3.py:45-50):**
```python
# Create S3 client (low-level service access)
s3_client = boto3.client('s3', region_name='us-east-1')  # Line 45
log_step("✅ Created S3 client", "Low-level API access")

# Create S3 resource (high-level object-oriented access)
s3_resource = boto3.resource('s3', region_name='us-east-1')  # Line 49
log_step("✅ Created S3 resource", "High-level OOP interface")
```

**Output:**
```
======================================================================
  1. Creating S3 Client and Resource
======================================================================
[10:52:53.345] ✅ Created S3 client              ← Line 45: Low-level API
             Low-level API access
[10:52:53.653] ✅ Created S3 resource           ← Line 49: High-level OOP
             High-level OOP interface
```

**💡 Key Insight:**
- **Client (Line 45):** Low-level API that maps directly to AWS API operations. Returns Python dictionaries.
- **Resource (Line 49):** High-level, object-oriented interface. More Pythonic and easier to use.
- **When to use Client:** Fine-grained control, newer AWS features, batch operations
- **When to use Resource:** Simple operations, more readable code, object-oriented approach

---

### 2. Creating Buckets

**Source Code (main_aws_s3.py:58-64):**
```python
bucket_name = 'my-demo-bucket-2024'
s3_client.create_bucket(Bucket=bucket_name)  # Line 58
log_step(f"📦 Created bucket: {bucket_name}")

# Create another bucket using resource interface
bucket_name_2 = 'my-second-bucket-2024'
bucket = s3_resource.create_bucket(Bucket=bucket_name_2)  # Line 63
```

**Output:**
```
======================================================================
  2. Creating S3 Buckets
======================================================================
[10:52:54.069] 📦 Created bucket: my-demo-bucket-2024      ← Line 58: Client method
[10:52:54.075] 📦 Created bucket: my-second-bucket-2024    ← Line 63: Resource method
             Using resource interface
```

**💡 Key Insight:**
- Both client and resource interfaces can create buckets
- Bucket names must be globally unique across all AWS accounts
- Bucket names must be DNS-compliant (lowercase, no underscores)

---

### 3. Listing Buckets

**Source Code (main_aws_s3.py:71-74):**
```python
response = s3_client.list_buckets()  # Line 71
log_step(f"🗂️  Found {len(response['Buckets'])} buckets:")
for bucket_info in response['Buckets']:  # Line 73
    log_step(f"   • {bucket_info['Name']}")
```

**Output:**
```
======================================================================
  3. Listing All Buckets
======================================================================
[10:52:54.080] 🗂️  Found 2 buckets:              ← Line 71: list_buckets() call
[10:52:54.080]    • my-demo-bucket-2024         ← Line 73: Iterating results
[10:52:54.080]    • my-second-bucket-2024
```

**💡 Key Insight:**
- `list_buckets()` returns all buckets in your AWS account
- Response contains a list of dictionaries with bucket metadata
- Each bucket has properties like Name, CreationDate

---

### 4. Uploading Objects

**Source Code (main_aws_s3.py:82-113):**
```python
# Upload string data
s3_client.put_object(  # Line 82
    Bucket=bucket_name,
    Key='data/hello.txt',
    Body='Hello from S3!',
    ContentType='text/plain'
)

# Upload JSON with metadata
json_data = {'name': 'boto3', 'version': '1.34', 'service': 's3'}
s3_client.put_object(  # Line 92
    Bucket=bucket_name,
    Key='data/config.json',
    Body=json.dumps(json_data),
    ContentType='application/json',
    Metadata={'author': 'demo-user', 'purpose': 'illustration'}  # Line 97
)

# Upload binary data
binary_data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR'  # PNG header
s3_client.put_object(  # Line 103
    Bucket=bucket_name,
    Key='images/sample.png',
    Body=binary_data,
    ContentType='image/png'
)

# Upload using resource interface
obj = s3_resource.Object(bucket_name, 'documents/readme.md')  # Line 112
obj.put(Body='# AWS S3 Demo\n\nThis is a demo file.')  # Line 113
```

**Output:**
```
======================================================================
  4. Uploading Objects to S3
======================================================================
[10:52:54.085] 📤 Uploaded: data/hello.txt       ← Line 82: String upload
             String content
[10:52:54.089] 📤 Uploaded: data/config.json    ← Line 92: JSON with metadata
             JSON with custom metadata
[10:52:54.092] 📤 Uploaded: images/sample.png   ← Line 103: Binary data
             Binary data
[10:52:54.097] 📤 Uploaded: documents/readme.md ← Line 113: Resource interface
             Using resource interface
```

**💡 Key Insight:**
- **Line 82:** Upload text directly as string
- **Line 97:** Add custom metadata as key-value pairs (useful for tagging)
- **Line 103:** Upload binary data (images, PDFs, etc.)
- **Line 113:** Resource interface provides cleaner syntax for simple operations
- The `Key` parameter acts as the file path within the bucket

---

### 5. Listing Objects with Filtering

**Source Code (main_aws_s3.py:121-133):**
```python
response = s3_client.list_objects_v2(Bucket=bucket_name)  # Line 121
log_step(f"📋 Found {response['KeyCount']} objects in '{bucket_name}':")
for obj in response.get('Contents', []):  # Line 123
    size_kb = obj['Size'] / 1024
    log_step(f"   • {obj['Key']:<30} ({size_kb:.2f} KB)")

# List objects with prefix filter
response = s3_client.list_objects_v2(  # Line 128
    Bucket=bucket_name,
    Prefix='data/'
)
```

**Output:**
```
======================================================================
  5. Listing Objects in Bucket
======================================================================
[10:52:54.106] 📋 Found 4 objects in 'my-demo-bucket-2024': ← Line 121: All objects
[10:52:54.106]    • data/config.json               (0.05 KB)
[10:52:54.106]    • data/hello.txt                 (0.01 KB)
[10:52:54.106]    • documents/readme.md            (0.03 KB)
[10:52:54.106]    • images/sample.png              (0.02 KB)
[10:52:54.109]
📋 Objects with prefix 'data/':                              ← Line 128: Filtered
[10:52:54.109]    • data/config.json
[10:52:54.109]    • data/hello.txt
```

**💡 Key Insight:**
- **Line 121:** `list_objects_v2()` is the recommended method (v2 is newer than v1)
- **Line 123:** Response contains object metadata (Size, LastModified, ETag, etc.)
- **Line 128:** Use `Prefix` parameter to filter objects like a directory structure
- S3 doesn't have real directories, but uses key prefixes to simulate them

---

### 6. Downloading Objects

**Source Code (main_aws_s3.py:142-159):**
```python
# Download to memory
response = s3_client.get_object(  # Line 142
    Bucket=bucket_name,
    Key='data/hello.txt'
)
content = response['Body'].read().decode('utf-8')  # Line 146

# Download JSON and parse
response = s3_client.get_object(Bucket=bucket_name, Key='data/config.json')
json_content = json.loads(response['Body'].read())  # Line 151

# Download using resource interface
obj = s3_resource.Object(bucket_name, 'documents/readme.md')  # Line 156
body = obj.get()['Body'].read().decode('utf-8')  # Line 157
```

**Output:**
```
======================================================================
  6. Downloading Objects from S3
======================================================================
[10:52:54.113] 📥 Downloaded: data/hello.txt              ← Line 142: get_object
             Content: 'Hello from S3!'                    ← Line 146: Decoded content
[10:52:54.116] 📥 Downloaded: data/config.json           ← Line 151: JSON parsed
             Parsed: {'name': 'boto3', 'version': '1.34', 'service': 's3'}
[10:52:54.120] 📥 Downloaded: documents/readme.md        ← Line 157: Resource method
             First line: # AWS S3 Demo
```

**💡 Key Insight:**
- **Line 142:** `get_object()` returns a response dictionary
- **Line 146:** Access content via `response['Body'].read()` (returns bytes)
- **Line 151:** Parse JSON directly after reading
- **Line 157:** Resource interface provides similar functionality
- For large files, consider using `download_file()` to stream to disk

---

### 7. Working with Object Metadata

**Source Code (main_aws_s3.py:166-175):**
```python
response = s3_client.head_object(  # Line 166
    Bucket=bucket_name,
    Key='data/config.json'
)
log_step("ℹ️  Metadata for 'data/config.json':")
log_step(f"   • Content-Type: {response['ContentType']}")  # Line 171
log_step(f"   • Content-Length: {response['ContentLength']} bytes")  # Line 172
log_step(f"   • Last-Modified: {response['LastModified']}")  # Line 173
log_step(f"   • ETag: {response['ETag']}")  # Line 174
log_step(f"   • Custom Metadata: {response.get('Metadata', {})}")  # Line 175
```

**Output:**
```
======================================================================
  7. Reading Object Metadata
======================================================================
[10:52:54.124] ℹ️  Metadata for 'data/config.json':
[10:52:54.124]    • Content-Type: application/json        ← Line 171: MIME type
[10:52:54.124]    • Content-Length: 53 bytes             ← Line 172: Size
[10:52:54.124]    • Last-Modified: 2025-11-04 10:52:54+00:00  ← Line 173: Timestamp
[10:52:54.124]    • ETag: "689523130579aff6862c4f9165bc5070"  ← Line 174: Hash
[10:52:54.124]    • Custom Metadata: {'author': 'demo-user', 'purpose': 'illustration'}  ← Line 175
```

**💡 Key Insight:**
- **Line 166:** `head_object()` retrieves metadata without downloading the object body
- **Line 171-174:** Standard HTTP metadata (Content-Type, size, modification time, ETag)
- **Line 175:** Custom metadata we added during upload (Line 97)
- More efficient than `get_object()` when you only need metadata

---

### 8. Generating Presigned URLs

**Source Code (main_aws_s3.py:183-197):**
```python
# Generate presigned URL for download (valid for 1 hour)
url = s3_client.generate_presigned_url(  # Line 183
    'get_object',
    Params={'Bucket': bucket_name, 'Key': 'data/hello.txt'},
    ExpiresIn=3600
)

# Generate presigned URL for upload
upload_url = s3_client.generate_presigned_url(  # Line 192
    'put_object',
    Params={'Bucket': bucket_name, 'Key': 'uploads/new-file.txt'},
    ExpiresIn=3600
)
```

**Output:**
```
======================================================================
  8. Generating Presigned URLs
======================================================================
[10:52:54.125] 🔗 Generated presigned URL for download:   ← Line 183: Download URL
             URL length: 150 characters (expires in 1 hour)
[10:52:54.125] 🔗 Generated presigned URL for upload:     ← Line 192: Upload URL
             Allows temporary upload access without credentials
```

**💡 Key Insight:**
- **Line 183:** Create temporary URLs for downloading objects without AWS credentials
- **Line 192:** Create temporary URLs for uploading objects
- `ExpiresIn` parameter sets validity duration in seconds (3600 = 1 hour)
- Useful for sharing files temporarily or allowing uploads from web browsers
- No authentication required to use the presigned URL within expiry time

---

### 9. Copying Objects

**Source Code (main_aws_s3.py:205-211):**
```python
copy_source = {'Bucket': bucket_name, 'Key': 'data/hello.txt'}  # Line 205
s3_client.copy_object(  # Line 206
    CopySource=copy_source,
    Bucket=bucket_name,
    Key='backup/hello-copy.txt'
)
```

**Output:**
```
======================================================================
  9. Copying Objects
======================================================================
[10:52:54.132] 📋 Copied object:                          ← Line 206: copy_object
             data/hello.txt → backup/hello-copy.txt
```

**💡 Key Insight:**
- **Line 206:** Copy objects within the same bucket or across buckets
- Server-side copy (no download/upload needed)
- Faster and more efficient than downloading and re-uploading
- Can copy between different buckets (even in different regions)

---

### 10. Deleting Objects

**Source Code (main_aws_s3.py:219-234):**
```python
# Delete single object
s3_client.delete_object(Bucket=bucket_name, Key='backup/hello-copy.txt')  # Line 219

# Delete multiple objects
objects_to_delete = {  # Line 223
    'Objects': [
        {'Key': 'data/hello.txt'},
        {'Key': 'data/config.json'},
        {'Key': 'images/sample.png'}
    ]
}
response = s3_client.delete_objects(  # Line 230
    Bucket=bucket_name,
    Delete=objects_to_delete
)
deleted_count = len(response.get('Deleted', []))  # Line 234
```

**Output:**
```
======================================================================
  10. Deleting Objects
======================================================================
[10:52:54.135] 🗑️  Deleted: backup/hello-copy.txt        ← Line 219: Single delete
[10:52:54.140] 🗑️  Deleted 3 objects                     ← Line 230: Batch delete
             Batch deletion                             ← Line 234: Count result
```

**💡 Key Insight:**
- **Line 219:** Delete single object with `delete_object()`
- **Line 230:** Batch delete up to 1000 objects with `delete_objects()`
- Batch deletion is more efficient than multiple single deletes
- Response contains list of deleted objects and any errors

---

### 11. Deleting Buckets

**Source Code (main_aws_s3.py:247-251):**
```python
# Delete bucket (must be empty)
s3_client.delete_bucket(Bucket=bucket_name)  # Line 247
log_step(f"🗑️  Deleted bucket: {bucket_name}")

s3_client.delete_bucket(Bucket=bucket_name_2)  # Line 250
```

**Output:**
```
======================================================================
  11. Deleting Buckets
======================================================================
[10:52:54.143] 🗑️  Deleted remaining object: documents/readme.md
[10:52:54.147] 🗑️  Deleted bucket: my-demo-bucket-2024   ← Line 247
[10:52:54.149] 🗑️  Deleted bucket: my-second-bucket-2024 ← Line 250
```

**💡 Key Insight:**
- **Line 247:** Buckets must be empty before deletion
- If bucket contains objects, deletion will fail
- Must delete all objects first, then delete the bucket

---

## Operations Summary

| Operation | Method | Interface | Key Use Case |
|-----------|--------|-----------|--------------|
| Create bucket | `create_bucket()` | Both | Initial setup |
| List buckets | `list_buckets()` | Client | View all buckets |
| Upload object | `put_object()` / `upload_file()` | Both | Store data |
| List objects | `list_objects_v2()` | Client | Browse bucket contents |
| Download object | `get_object()` / `download_file()` | Both | Retrieve data |
| Get metadata | `head_object()` | Client | Check properties |
| Copy object | `copy_object()` | Client | Duplicate/move data |
| Delete object | `delete_object()` | Both | Remove single file |
| Batch delete | `delete_objects()` | Client | Remove multiple files |
| Presigned URL | `generate_presigned_url()` | Client | Temporary access |
| Delete bucket | `delete_bucket()` | Both | Cleanup |

## Key Takeaways

1. **Two Interfaces:** boto3 provides both Client (low-level) and Resource (high-level) APIs
2. **Bucket Operations:** Create, list, and delete buckets (must be empty to delete)
3. **Object Operations:** Upload, download, list, copy, and delete objects
4. **Metadata:** Attach custom metadata during upload, retrieve without downloading content
5. **Presigned URLs:** Generate temporary URLs for secure, credential-free access
6. **Batch Operations:** Use `delete_objects()` for efficient bulk deletions
7. **Prefix Filtering:** Simulate directory structure using key prefixes

## Common Use Cases

✅ **Good for:**
- Storing and retrieving files (backups, media, documents)
- Hosting static websites
- Data lakes and big data storage
- Application data storage
- Cross-region replication
- Temporary file sharing via presigned URLs

## Best Practices

1. **Use `list_objects_v2()`** instead of deprecated `list_objects()`
2. **Add metadata** to objects for better organization and searchability
3. **Use presigned URLs** for temporary access instead of making objects public
4. **Batch operations** when deleting multiple objects for better performance
5. **Handle pagination** when listing large numbers of objects
6. **Use appropriate storage classes** (Standard, Infrequent Access, Glacier) based on access patterns
7. **Enable versioning** for important buckets to protect against accidental deletions
