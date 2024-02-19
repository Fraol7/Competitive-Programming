class Solution:
    def simplifyPath(self, path):
        files = []
        path = path.split("/")
        for elem in path:
            if files and elem == "..":
                files.pop()
            elif elem not in [".", "", ".."]:
                files.append(elem)
        return "/" + "/".join(files)