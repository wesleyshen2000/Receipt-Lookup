class FolderLocationConstants():
    root = "../../"
    tmp = root + "tmp/"

    @staticmethod
    def get_temp_folder():
        return FolderLocationConstants.tmp

    @staticmethod
    def get_root_dir():
        return FolderLocationConstants.root