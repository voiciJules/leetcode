class Solution:
    def simplifyPath(self, path: str) -> str:
        dir = path.split('/')
        while '' in dir:
            dir.remove('')

        while '.' in dir:
            dir.remove('.')

        while '..' in dir:
            idx = dir.index('..')
            if idx != 0:
                del dir[idx-1]
            dir.remove('..')
        # print(dir)
        simplified_path = "/" + ('/').join(dir)
        return simplified_path