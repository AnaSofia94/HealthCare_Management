from django.contrib.staticfiles.finders import FileSystemFinder

class DRFStaticFinder(FileSystemFinder):
    def find(self, path, all=False):
        # Correct the DRF-YASG static file path
        if path.startswith('drf-yasg-yasg/'):
            path = path.replace('drf-yasg-yasg/', 'drf-yasg/')
        return super().find(path, all=all)

    def list(self, ignore_patterns):
        # Use the parent class's implementation for listing files
        return super().list(ignore_patterns)