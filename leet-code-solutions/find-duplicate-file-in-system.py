class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_dict = defaultdict(list)
        for path in paths:
            files = path.split(' ')
            directory = files[0]
            
            for file in files[1:]:
                name, content = file.split('(')
                content_dict[content[:-1]].append(directory + '/' + name)
        
        result = [content_dict[content] for content in content_dict if len(content_dict[content]) > 1]
        return result
