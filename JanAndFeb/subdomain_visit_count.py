class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashMap = defaultdict(int)
        output = []

        for cpdomain in cpdomains:
            repetition, domains = [x for x in cpdomain.split()] #rep = 9001, domains = "discuss.leetcode.com"
            subDomain = [x for x in domains.split(".")]  #subDomains = ["discuss", "leetcode", "com"]
            print(repetition, domains )
            print(subDomain)

            d1 = ".".join(subDomain[:]) #d1 ="discuss.leetcode.com"
            d2 = ".".join(subDomain[1:]) #d2 ="leetcode.com"

            hashMap[d1] = hashMap.get(d1, 0) + int(repetition)
            hashMap[d2] = hashMap.get(d2, 0) + int(repetition)
            if len(subDomain) == 3:
                d3 = subDomain[2] #d3 ="com"
                hashMap[d3] = hashMap.get(d3, 0) + int(repetition)

        for domain, rep in hashMap.items():
            output.append(f"{rep} {domain}")

        return output


            