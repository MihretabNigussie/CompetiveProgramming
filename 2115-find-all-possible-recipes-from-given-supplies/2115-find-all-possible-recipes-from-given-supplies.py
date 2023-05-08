class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        graph = defaultdict(list)
        queue = deque(supplies)
        lst = []
        incoming = defaultdict(int)
        recipeSet = set(recipes)
        
        for i in range(len(recipes)):
            recipe = recipes[i]
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipe)
                incoming[recipe] += 1
    
        while queue:
            recipe = queue.popleft()
            if recipe in recipeSet:
                lst.append(recipe)
            
            for neighbour in graph[recipe]:
                incoming[neighbour] -= 1
                
                if incoming[neighbour] == 0:
                    queue.append(neighbour)   
        return lst
                
            
            
        
        
        
        
        
        