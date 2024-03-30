import os
from bootstrap.app import AppBootstrap
from config.filesystem import FilesystemConfiguration
from laraflask.Helpers.config import Config

# Import driver
from laraflask.Drivers.Storage.Local import StorageDrivers

class Storage:

    def __init__(self, driver = None):
        self.driver = driver if driver else FilesystemConfiguration().default
        self.LocalStorageDrivers = StorageDrivers(AppBootstrap, self.disk_configuration('local'))
        self.PublicStorageDrivers = StorageDrivers(AppBootstrap, self.disk_configuration('public'))
        return
    
    # Get storage path
    def path(self, path = None):
        # If driver is local 
        if self.driver == 'local':
            return self.LocalStorageDrivers.path(path)
        
        # If driver is public
        elif self.driver == 'public':
            return self.PublicStorageDrivers.path(path)

        raise None
    
    # Get storage url path
    def url_path(self, path = None):
        # If driver is local
        if self.driver == 'local':
            return self.LocalStorageDrivers.url_path(path)
        
        # If driver is public
        elif self.driver == 'public':
            return self.PublicStorageDrivers.url_path(path)

        return None
    
    # Get file path
    def file(self, path):
        # If driver is local or public
        if self.driver == 'local':
            return self.LocalStorageDrivers.file(path)
        
        # If driver is public
        elif self.driver == 'public':
            return self.PublicStorageDrivers.file(path)

        return None
    
    # Check if file exists
    def exists(self, path):
        # If driver is local
        if self.driver == 'local':
            return self.LocalStorageDrivers.exists(path)
        
        # If driver is public
        elif self.driver == 'public':
            return self.PublicStorageDrivers.exists(path)

        return None
    
    # Get file contents
    def get(self, path):
        # If driver is local 
        if self.driver == 'local':
            return self.LocalStorageDrivers.get(path)
        
        # If driver is public
        elif self.driver == 'public':
            return self.PublicStorageDrivers.get(path)

        return None
        
    # Write file contents
    def put(self, path, contents):
        # If driver is local
        if self.driver == 'local':
            return self.LocalStorageDrivers.put(path, contents)
        
        # If driver is public
        elif self.driver == 'public':
            return self.PublicStorageDrivers.put(path, contents)

        return None

    # Delete file
    def delete(self, path):
        # If driver is local
        if self.driver == 'local':
            return self.LocalStorageDrivers.delete(path)
        
        # If driver is public
        elif self.driver == 'public':
            return self.PublicStorageDrivers.delete(path)

        return None

    # Move file to storage
    def move(self, path, new_path):
        # If driver is local
        if self.driver == 'local': 
            return self.LocalStorageDrivers.move(path, new_path)
        
        # If driver is public
        elif self.driver == 'public':
            return self.PublicStorageDrivers.move(path, new_path)

        return None

    # Copy file to storage
    def copy(self, path, new_path):
        # If driver is local
        if self.driver == 'local':
            return self.LocalStorageDrivers.copy(path, new_path)
        
        # If driver is public
        elif self.driver == 'public':
            return self.PublicStorageDrivers.copy(path, new_path)

        return None

    # Store file in storage
    def store(self, path, file, filename = None):
        # If driver is local
        if self.driver == 'local':
            return self.LocalStorageDrivers.store(path, file, filename)
        
        # If driver is public
        elif self.driver == 'public':
            return self.PublicStorageDrivers.store(path, file, filename)

        return None

    # Create directory
    def make_directory(self, path):
        # If driver is local 
        if self.driver == 'local':
            return self.LocalStorageDrivers.make_directory(path)
        
        # If driver is public
        elif self.driver == 'public':
            return self.PublicStorageDrivers.make_directory(path)
        
        return None

    # Delete directory
    def delete_directory(self, path):
        # If driver is local 
        if self.driver == 'local':
            return self.LocalStorageDrivers.delete_directory(path)
        
        # If driver is public
        elif self.driver == 'public':
            return self.PublicStorageDrivers.delete_directory(path)
        
        return None

    # Delete directory and all its contents recursively
    def delete_directory_recursive(self, path):
        # If driver is local 
        if self.driver == 'local':
            return self.LocalStorageDrivers.delete_directory_recursive(path)
        
        # If driver is public
        elif self.driver == 'public':
            return self.PublicStorageDrivers.delete_directory_recursive(path)
        
        return None

    # Get all files in directory
    def files(self, path):
        # If driver is local
        if self.driver == 'local':
            return self.LocalStorageDrivers.files(path)
        
        # If driver is public
        elif self.driver == 'public':
            return self.PublicStorageDrivers.files(path)
        
        return None

    # Get all directories in directory
    def directories(self, path):
        # If driver is local
        if self.driver == 'local':
            return self.LocalStorageDrivers.directories(path)
        
        # If driver is public
        elif self.driver == 'public':
            return self.PublicStorageDrivers.directories(path)
        
        return None
    
    # Get all files and directories in directory
    def all(self, path):
        # If driver is local 
        if self.driver == 'local':
            return self.LocalStorageDrivers.all(path)
        
        # If driver is public
        elif self.driver == 'public':
            return self.PublicStorageDrivers.all(path)
        
        return None
    
    # Get all files in directory recursively
    def all_files(self, path):
        # If driver is local
        if self.driver == 'local':
            return self.LocalStorageDrivers.all_files(path)
        
        # If driver is public
        elif self.driver == 'public':
            return self.PublicStorageDrivers.all_files(path)
        
        return None
    
    # Get all directories in directory recursively
    def all_directories(self, path):
        # If driver is local
        if self.driver == 'local':
            return self.LocalStorageDrivers.all_directories(path)
        
        # If driver is public
        elif self.driver == 'public':
            return self.PublicStorageDrivers.all_directories(path)
        
        return None
    
    # Get all files and directories in directory recursively
    def all_recursive(self, path):
        # If driver is local
        if self.driver == 'local':
            return self.LocalStorageDrivers.all_recursive(path)
        
        # If driver is public
        elif self.driver == 'public':
            return self.PublicStorageDrivers.all_recursive(path)
        
        return None
    
    # Get all files with a given extension in directory
    def files_with_extension(self, path, extension):
        # If driver is local
        if self.driver == 'local':
            return self.LocalStorageDrivers.files_with_extension(path, extension)
        
        # If driver is public
        elif self.driver == 'public':
            return self.PublicStorageDrivers.files_with_extension(path, extension)
        
        return None
    
    # Get all files with a given extension in directory recursively
    def all_files_with_extension(self, path, extension):
        # If driver is local
        if self.driver == 'local':
            return self.LocalStorageDrivers.all_files_with_extension(path, extension)
        
        # If driver is public
        elif self.driver == 'public':
            return self.PublicStorageDrivers.all_files_with_extension(path, extension)
        
        return None
    
    # Get all files with a given extension in directory
    def directories_with_extension(self, path, extension):
        # If driver is local
        if self.driver == 'local':
            return self.LocalStorageDrivers.directories_with_extension(path, extension)
        
        # If driver is public
        elif self.driver == 'public':
            return self.PublicStorageDrivers.directories_with_extension(path, extension)
        
        return None
    
    # Get all files with a given extension in directory recursively
    def all_directories_with_extension(self, path, extension):
        # If driver is local
        if self.driver == 'local':
            return self.LocalStorageDrivers.all_directories_with_extension(path, extension)
        
        # If driver is public
        elif self.driver == 'public':
            return self.PublicStorageDrivers.all_directories_with_extension(path, extension)

        return None
    
    # Get disk configuration
    def disk_configuration(self, driver = None):
        config = {};

        # Append base url
        config['base_url'] = Config().get('app.app_host') + ':' + str(Config().get('app.app_port'))

        if driver:
            for key, value in FilesystemConfiguration().disks[driver].items():
                config[key] = value
        
        for key, value in FilesystemConfiguration().disks[self.driver].items():
            config[key] = value

        return config

# Path: laraflask/Helpers/storage.py