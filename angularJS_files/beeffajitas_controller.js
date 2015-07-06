app.controller('RecipeController', function($scope) {
	$scope.test = "working!"
	$scope.BeefFajitas = {
		name: "Beef Fajitas",
		//not sure if this works for the img...looking into it
		img: "https://api.pearson.com/kitchen-manager/v1/images/full/beef_fajitas.jpg",
		serving: "Serves 6, Yields 6",
		ingredients: [
			"4 garlic cloves",
			"1 1/2 tsp salt",
			"1 1/2 tsp whole black pepper", 
			"1 1/2 tsp ground cumin", 
			"1 1/2 tsp onion powder",
			"1 1/2 tsp chili powder", 
			"2 lb beef skirt steak",
			"2 tbl vegetable oil",
			"1 red bell pepper",
			"1 yellow bell pepper",
			"1 green bell pepper",
			"1 onion",
			"2 garlic cloves",
			"6 sprigs fresh cilantro",
		],
		directions: "Make the marinade by chopping and mashing the garlic into a paste. In a bowl, combine the garlic paste with the remaining marinade ingredients.Trim the fat from the skirt steak. Cut the steak into two or three pieces if necessary. Add the steaks to the marinade, turning them several times to coat all sides. Cover the steak and mari-nate in the refrigerator for at least 1 hour or overnight. Grill the steak on a hot grill to the desired doneness. Remove the steak and allow it to rest for 10 minutes. Add the oil to a heavy sautee pan, heat the pan until very hot and sautee the bell peppers, onion and garlic just until they begin to soften. Slice the steak against the grain into thin slices. Arrange the steak and the pepper mixture on very hot cast-iron platters and garnish with the cilantro. The platters should be sizzling as they are presented to the table. Serve the fajitas accompanied by warm flour or corn tortillas, fresh salsa, sour cream, and guacamole.",
		nutritional_info: [

		]
	}
	$scope.recipeblurb = "Mexican Cuisine # will link to all Mexican cuisine recipes (grid of linkable pictures with recipe names)"

});