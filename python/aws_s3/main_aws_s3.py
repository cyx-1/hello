# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "boto3>=1.34.0",
#     "moto[s3]>=5.0.0",
# ]
# ///
"""
Boto3 AWS S3 Example: Comprehensive S3 Operations

This example demonstrates common AWS S3 operations using the boto3 library.
It uses moto for mocking AWS services, allowing the code to run without
actual AWS credentials or costs.
"""

import json
from datetime import datetime

import boto3
from moto import mock_aws


def log_section(title: str) -> None:
    """Print a formatted section header."""
    print(f"\n{'=' * 70}")
    print(f"  {title}")
    print("=" * 70)


def log_step(step: str, detail: str = "") -> None:
    """Print a formatted step message."""
    timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    if detail:
        print(f"[{timestamp}] {step}")
        print(f"             {detail}")
    else:
        print(f"[{timestamp}] {step}")


@mock_aws
def demonstrate_s3_operations():
    """Demonstrate comprehensive S3 operations using boto3."""

    # ========================================================================
    # 1. Initialize S3 Client and Resource
    # ========================================================================
    log_section("1. Creating S3 Client and Resource")

    # Create S3 client (low-level service access)
    s3_client = boto3.client("s3", region_name="us-east-1")  # Line 45
    log_step("✅ Created S3 client", "Low-level API access")

    # Create S3 resource (high-level object-oriented access)
    s3_resource = boto3.resource("s3", region_name="us-east-1")  # Line 49
    log_step("✅ Created S3 resource", "High-level OOP interface")

    # ========================================================================
    # 2. Create Buckets
    # ========================================================================
    log_section("2. Creating S3 Buckets")

    bucket_name = "my-demo-bucket-2024"
    s3_client.create_bucket(Bucket=bucket_name)  # Line 58
    log_step(f"📦 Created bucket: {bucket_name}")

    # Create another bucket using resource interface
    bucket_name_2 = "my-second-bucket-2024"
    s3_resource.create_bucket(Bucket=bucket_name_2)  # Line 63
    log_step(f"📦 Created bucket: {bucket_name_2}", "Using resource interface")

    # ========================================================================
    # 3. List All Buckets
    # ========================================================================
    log_section("3. Listing All Buckets")

    response = s3_client.list_buckets()  # Line 71
    log_step(f"🗂️  Found {len(response['Buckets'])} buckets:")
    for bucket_info in response["Buckets"]:  # Line 73
        log_step(f"   • {bucket_info['Name']}")

    # ========================================================================
    # 4. Upload Objects to S3
    # ========================================================================
    log_section("4. Uploading Objects to S3")

    # Upload string data
    s3_client.put_object(  # Line 82
        Bucket=bucket_name,
        Key="data/hello.txt",
        Body="Hello from S3!",
        ContentType="text/plain",
    )
    log_step("📤 Uploaded: data/hello.txt", "String content")

    # Upload JSON data
    json_data = {"name": "boto3", "version": "1.34", "service": "s3"}
    s3_client.put_object(  # Line 92
        Bucket=bucket_name,
        Key="data/config.json",
        Body=json.dumps(json_data),
        ContentType="application/json",
        Metadata={"author": "demo-user", "purpose": "illustration"},  # Line 97
    )
    log_step("📤 Uploaded: data/config.json", "JSON with custom metadata")

    # Upload binary data (simulated file)
    binary_data = b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR"  # PNG header
    s3_client.put_object(  # Line 103
        Bucket=bucket_name,
        Key="images/sample.png",
        Body=binary_data,
        ContentType="image/png",
    )
    log_step("📤 Uploaded: images/sample.png", "Binary data")

    # Upload using resource interface
    obj = s3_resource.Object(bucket_name, "documents/readme.md")  # Line 112
    obj.put(Body="# AWS S3 Demo\n\nThis is a demo file.")  # Line 113
    log_step("📤 Uploaded: documents/readme.md", "Using resource interface")

    # ========================================================================
    # 5. List Objects in a Bucket
    # ========================================================================
    log_section("5. Listing Objects in Bucket")

    response = s3_client.list_objects_v2(Bucket=bucket_name)  # Line 121
    log_step(f"📋 Found {response['KeyCount']} objects in '{bucket_name}':")
    for obj in response.get("Contents", []):  # Line 123
        size_kb = obj["Size"] / 1024
        log_step(f"   • {obj['Key']:<30} ({size_kb:.2f} KB)")

    # List objects with prefix filter
    response = s3_client.list_objects_v2(  # Line 128
        Bucket=bucket_name, Prefix="data/"
    )
    log_step("\n📋 Objects with prefix 'data/'")
    for obj in response.get("Contents", []):
        log_step(f"   • {obj['Key']}")

    # ========================================================================
    # 6. Download Objects from S3
    # ========================================================================
    log_section("6. Downloading Objects from S3")

    # Download to memory
    response = s3_client.get_object(  # Line 142
        Bucket=bucket_name, Key="data/hello.txt"
    )
    content = response["Body"].read().decode("utf-8")  # Line 146
    log_step("📥 Downloaded: data/hello.txt", f"Content: '{content}'")

    # Download JSON and parse
    response = s3_client.get_object(Bucket=bucket_name, Key="data/config.json")
    json_content = json.loads(response["Body"].read())  # Line 151
    log_step("📥 Downloaded: data/config.json", f"Parsed: {json_content}")

    # Download using resource interface
    obj = s3_resource.Object(bucket_name, "documents/readme.md")  # Line 156
    body = obj.get()["Body"].read().decode("utf-8")  # Line 157
    log_step(
        "📥 Downloaded: documents/readme.md", f"First line: {body.split(chr(10))[0]}"
    )

    # ========================================================================
    # 7. Working with Object Metadata
    # ========================================================================
    log_section("7. Reading Object Metadata")

    response = s3_client.head_object(  # Line 166
        Bucket=bucket_name, Key="data/config.json"
    )
    log_step("ℹ️  Metadata for 'data/config.json':")
    log_step(f"   • Content-Type: {response['ContentType']}")  # Line 171
    log_step(f"   • Content-Length: {response['ContentLength']} bytes")  # Line 172
    log_step(f"   • Last-Modified: {response['LastModified']}")  # Line 173
    log_step(f"   • ETag: {response['ETag']}")  # Line 174
    log_step(f"   • Custom Metadata: {response.get('Metadata', {})}")  # Line 175

    # ========================================================================
    # 8. Generate Presigned URLs
    # ========================================================================
    log_section("8. Generating Presigned URLs")

    # Generate presigned URL for download (valid for 1 hour)
    url = s3_client.generate_presigned_url(  # Line 183
        "get_object",
        Params={"Bucket": bucket_name, "Key": "data/hello.txt"},
        ExpiresIn=3600,
    )
    log_step(
        "🔗 Generated presigned URL for download:",
        f"URL length: {len(url)} characters (expires in 1 hour)",
    )

    # Generate presigned URL for upload
    s3_client.generate_presigned_url(  # Line 192
        "put_object",
        Params={"Bucket": bucket_name, "Key": "uploads/new-file.txt"},
        ExpiresIn=3600,
    )
    log_step(
        "🔗 Generated presigned URL for upload:",
        "Allows temporary upload access without credentials",
    )

    # ========================================================================
    # 9. Copy Objects
    # ========================================================================
    log_section("9. Copying Objects")

    copy_source = {"Bucket": bucket_name, "Key": "data/hello.txt"}  # Line 205
    s3_client.copy_object(  # Line 206
        CopySource=copy_source, Bucket=bucket_name, Key="backup/hello-copy.txt"
    )
    log_step("📋 Copied object:", "data/hello.txt → backup/hello-copy.txt")

    # ========================================================================
    # 10. Delete Objects
    # ========================================================================
    log_section("10. Deleting Objects")

    # Delete single object
    s3_client.delete_object(Bucket=bucket_name, Key="backup/hello-copy.txt")  # Line 219
    log_step("🗑️  Deleted: backup/hello-copy.txt")

    # Delete multiple objects
    objects_to_delete = {  # Line 223
        "Objects": [
            {"Key": "data/hello.txt"},
            {"Key": "data/config.json"},
            {"Key": "images/sample.png"},
        ]
    }
    response = s3_client.delete_objects(  # Line 230
        Bucket=bucket_name, Delete=objects_to_delete
    )
    deleted_count = len(response.get("Deleted", []))  # Line 234
    log_step(f"🗑️  Deleted {deleted_count} objects", "Batch deletion")

    # ========================================================================
    # 11. Delete Buckets
    # ========================================================================
    log_section("11. Deleting Buckets")

    # Delete remaining objects first
    s3_client.delete_object(Bucket=bucket_name, Key="documents/readme.md")
    log_step("🗑️  Deleted remaining object: documents/readme.md")

    # Delete bucket (must be empty)
    s3_client.delete_bucket(Bucket=bucket_name)  # Line 247
    log_step(f"🗑️  Deleted bucket: {bucket_name}")

    s3_client.delete_bucket(Bucket=bucket_name_2)  # Line 250
    log_step(f"🗑️  Deleted bucket: {bucket_name_2}")

    # ========================================================================
    # Final Summary
    # ========================================================================
    log_section("✅ Demo Complete!")
    print("\nKey boto3 S3 operations demonstrated:")
    print("  1. Client vs Resource interfaces")
    print("  2. Creating and listing buckets")
    print("  3. Uploading objects (text, JSON, binary)")
    print("  4. Listing objects with filtering")
    print("  5. Downloading objects")
    print("  6. Working with metadata")
    print("  7. Generating presigned URLs")
    print("  8. Copying objects")
    print("  9. Deleting objects and buckets")


if __name__ == "__main__":
    demonstrate_s3_operations()
