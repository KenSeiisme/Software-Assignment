    def search_recipe(self):
        search_text = self.search_entry.get().strip().lower()

        search_results = [
            recipe for recipe in recipes
            if search_text in recipe["name"].lower()
            or search_text in recipe.get("category", "").lower()
            or any(
                search_text in tag.lower()
                for tag in recipe.get("tags", [])
            )
        ]

        self.display_Recipes(search_results)