class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        refer = defaultdict(int)
        result = []
        for cpdomain in cpdomains:
            cpdomain = list(map(str, cpdomain.split()))
            n, domain = cpdomain[0], cpdomain[1]
            domain = list(map(str, domain.split(".")))
            print(domain)
            for link in range(len(domain)):
                address = domain[link:]
                adr = '.'.join(address)
                refer[adr] += int(n)
        for key in refer:
            result.append(str(refer[key])+" "+str(key))
        return result
