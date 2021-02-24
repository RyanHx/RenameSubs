import os


def for_current_dir():
    dir_path = os.getcwd()
    dirFiles = os.listdir(dir_path)
    vidFiles = []
    subFiles = []
    sub_format = '.srt'
    for name in dirFiles:
        if name.endswith('.mp4') or name.endswith('.mkv') or name.endswith('.avi'):
            vidFiles.append(name)
        elif name.endswith(sub_format):
            subFiles.append(name)
    rename_files(dir_path, vidFiles, subFiles, sub_format)
    return


def rename_files(path, vidFiles, subFiles, sub_format):
    vidFiles.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
    subFiles.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
    os.chdir(path)
    try:
        assert (len(subFiles) == len(vidFiles))
        for i, vname in enumerate(vidFiles):
            print("{0} renamed to {1} ".format(subFiles[i], os.path.splitext(vname)[0]))
            os.rename(subFiles[i], os.path.splitext(vname)[0] + sub_format)
    except AssertionError:
        print(len(subFiles))
        print(len(vidFiles))
    return


def main():
    for_current_dir()


main()
