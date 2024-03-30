import os

import urllib

class StorageDrivers:

    def __init__(self, bootstrap, configuration):
        self.bootstrap = bootstrap
        self.configuration = configuration
        return
    
    # Get storage path
    def path(self, path = None):
        return os.path.join(self.configuration['root'], path) if path else self.configuration['root']
    
    # Get storage url path
    def url_path(self, path = None):
        # Replace string in self.configuration['root'] with self.bootstrap.app_base_path
        storage_url = self.configuration['root'].replace(self.bootstrap().app_base_path, self.configuration['base_url'])

        # Replace /resources/static/storage with /assets/storage
        storage_url = storage_url.replace('/resources/static/storage', '/assets/storage')

        # url encode the path
        path = urllib.parse.quote(path) if path else None

        # Return storage_url + '/' + path if path else storage_url
        return storage_url + '/' + path if path else storage_url
    
    # Get file path
    def file(self, path):
        return self.path(path)
    
    # Check if file exists
    def exists(self, path):
        return os.path.exists(self.file(path))
    
    # Get file contents
    def get(self, path):
        with open(self.file(path), 'r') as file:
            return file.read()
        
    # Write file contents
    def put(self, path, contents):
        with open(self.file(path), 'w') as file:
            file.write(contents)

    # Delete file
    def delete(self, path):
        os.remove(self.file(path))

    # Move file to storage
    def move(self, path, new_path):
        os.rename(self.file(path), self.file(new_path))

    # Copy file to storage
    def copy(self, path, new_path):
        import shutil
        shutil.copy(self.file(path), self.file(new_path))

    # Store file in storage
    def store(self, path, file, filename=None):
        # check directory
        if not os.path.exists(self.path(path)):
            self.make_directory(path)
            
        if filename:
            file.save(self.file(os.path.join(path, filename)))
            return filename
        else:
            file.save(self.file(os.path.join(path, file.filename)))
            return file.filename

    # Create directory
    def make_directory(self, path):
        os.makedirs(self.path(path), exist_ok=True)

    # Delete directory
    def delete_directory(self, path):
        os.rmdir(self.path(path))

    # Delete directory and all its contents recursively
    def delete_directory_recursive(self, path):
        import shutil
        shutil.rmtree(self.path(path))

    # Get all files in directory
    def files(self, path):
        return [f for f in os.listdir(self.path(path)) if os.path.isfile(os.path.join(self.path(path), f))]

    # Get all directories in directory
    def directories(self, path):
        return [f for f in os.listdir(self.path(path)) if os.path.isdir(os.path.join(self.path(path), f))]
    
    # Get all files and directories in directory
    def all(self, path):
        return [f for f in os.listdir(self.path(path))]
    
    # Get all files in directory recursively
    def all_files(self, path):
        files = []
        for root, directories, files in os.walk(self.path(path)):
            for file in files:
                files.append(os.path.join(root, file))
        return files
    
    # Get all directories in directory recursively
    def all_directories(self, path):
        directories = []
        for root, directories, files in os.walk(self.path(path)):
            for directory in directories:
                directories.append(os.path.join(root, directory))
        return directories
    
    # Get all files and directories in directory recursively
    def all_recursive(self, path):
        all = []
        for root, directories, files in os.walk(self.path(path)):
            for directory in directories:
                all.append(os.path.join(root, directory))
            for file in files:
                all.append(os.path.join(root, file))
        return all
    
    # Get all files with a given extension in directory
    def files_with_extension(self, path, extension):
        return [f for f in os.listdir(self.path(path)) if os.path.isfile(os.path.join(self.path(path), f)) and f.endswith(extension)]
    
    # Get all files with a given extension in directory recursively
    def all_files_with_extension(self, path, extension):
        files = []
        for root, directories, files in os.walk(self.path(path)):
            for file in files:
                if file.endswith(extension):
                    files.append(os.path.join(root, file))
        return files
    
    # Get all files with a given extension in directory
    def directories_with_extension(self, path, extension):
        return [f for f in os.listdir(self.path(path)) if os.path.isdir(os.path.join(self.path(path), f)) and f.endswith(extension)]
    
    # Get all files with a given extension in directory recursively
    def all_directories_with_extension(self, path, extension):
        directories = []
        for root, directories, files in os.walk(self.path(path)):
            for directory in directories:
                if directory.endswith(extension):
                    directories.append(os.path.join(root, directory))
        return directories