class VideoUploader:
    def upload(self, file_path):
        print(f"Uploading video from {file_path}...")
        # فرض کنید ویدیو آپلود شده است و لینک آن را برمی‌گردانیم
        return "http://example.com/video.mp4"

class VideoConverter:
    def convert_to_mp4(self, video_url):
        print(f"Converting video at {video_url} to MP4 format...")
        # فرض کنید ویدیو تبدیل شده است و لینک ویدیو MP4 را برمی‌گردانیم
        return "http://example.com/video_converted.mp4"

class VideoMetadata:
    def extract_metadata(self, video_url):
        print(f"Extracting metadata from video at {video_url}...")
        # فرض کنید متادیتای ویدیو را استخراج کردیم
        return {"title": "Example Video", "duration": "5 minutes"}