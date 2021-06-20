class FolderLocationConstants():
    root = "../../"
    tmp = root + "tmp/"

    def get_temp_folder(self):
        return self.tmp

    def get_root_dir(self):
        return self.root