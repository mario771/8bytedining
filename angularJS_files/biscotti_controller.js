app.controller('RecipeController', function($scope) {
	$scope.test = "working!"
	$scope.Biscotti = {
		name: "Biscotti",
		//not sure if this works for the img...looking into it
		img: "https://api.pearson.com/kitchen-manager/v1/images/full/biscotti.jpg",
		serving: "Serves 36, Yields 36",
		ingredients: [
			"1 tbl ground cinnamon",
    		"2 tsp baking powder",
    		"10 oz hazelnut flour",
    		"3 oz almond flour",
    		"1 lb pastry flour",
    		"5 eggs",
    		"1 lb granulated sugar",
    		"8 oz unsalted butter",
    		"10 oz whole unblanched hazelnuts",
    		"semisweet chocolate (as needed)",
		],
		directions: "Sift together the cinnamon and ammonium carbonate or baking powder. Stir in the hazelnut, almond and pastry flours. Set aside. In a large bowl, whisk together the eggs and sugar to the ribbon stage, approximately 3 minutes. Add the butter. Stir in the flour mixture with a rubber spatula, then stir in the whole hazelnuts. Divide the dough into three even pieces. Refrigerate until cold. Roll each piece of dough into a 12-inch (30-centimeter) log. Place on a paper-lined sheet pan, leaving at least 3 inches (7.5 centimeters) of space between each log. Bake at 350F (180C) until golden in color, approximately 20 minutes. Cool the logs, then slice them into 1-inch- (3-centimeter-) thick slices. Place the sliced cookies upright on paper-lined sheet pans. Double-tray the pans. Reduce heat to 325F (160C) and bake until the biscotti are thoroughly crisp, approximately 40 minutes. Once cool, the biscotti may be dipped in tempered chocolate.",
		nutritional_info: [
			
		]
	}
	$scope.recipeblurb = "Italian Cuisine # will link to all Italian cuisine recipes (grid of linkable pictures with recipe names)"

});