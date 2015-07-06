app.controller('RecipeController', function($scope) {
	$scope.test = "working!"
	$scope.AuntRuthiesPotRoast = {
		name: "Aunt Ruthie's Pot Roast",
		//not sure if this works for the img...looking into it
		img: "https://api.pearson.com/kitchen-manager/v1/images/full/aunt_ruthies_pot_roast.jpg",
		ingredients: [
			"3 fl oz vegetable oil",
			"6 lb beef brisket",
			"3 lb onion",
			"2 tbl garlic",
			"1 qt Brown Veal Stock",
			"1 pt tomato sauce",
			"4 oz light brown sugar",
			"1 tsp paprika",
			"2 tsp dry mustard",
			"8 fl oz Lemon Juice (fresh)",
			"8 oz ketchup",
			"8 fl oz red wine vinegar",
			"2 fl oz worcestershire sauce",
			"salt (to taste)",
			"ground black pepper (to taste)"
		],
		directions: "Heat the oil in a large rondeau. Add the beef and brown thoroughly. Remove and reserve the brisket.Add the onions and garlic to the pan and sautee. Add the stock and tomato sauce to the pan.Return the brisket to the pan, cover tightly and bring to a boil.Braise at 325F (160C) for 1 and 1/2 hours, basting or turning the brisket often. Combine the remaining ingredients and add to the pan. Continue cooking and basting the brisket until tender, approximately 1 hour. Add additional stock or water as needed during braising. Remove the brisket, degrease the sauce and adjust its consistency and seasonings. Do not strain the sauce.Slice the brisket against the grain and serve with the sauce.",
		nutritional_info: [
			
		]
	}
	$scope.recipeblurb = "American Cuisine # will link to all American cuisine recipes (grid of linkable pictures with recipe names)"

});
