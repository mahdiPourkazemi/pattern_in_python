from vid_subsystem import VideoUploader,VideoConverter,VideoMetadata


class VideoFacade:
    def __init__(self):
        self.uploader = VideoUploader()
        self.converter = VideoConverter()
        self.metadata = VideoMetadata()

    def process_video(self, file_path):
        print("Starting video processing...")

        # مرحله 1: آپلود ویدیو
        video_url = self.uploader.upload(file_path)

        # مرحله 2: تبدیل ویدیو به فرمت MP4
        converted_video_url = self.converter.convert_to_mp4(video_url)

        # مرحله 3: استخراج متادیتا
        metadata = self.metadata.extract_metadata(converted_video_url)

        print("Video processing completed.")
        return {
            "video_url": converted_video_url,
            "metadata": metadata
        }