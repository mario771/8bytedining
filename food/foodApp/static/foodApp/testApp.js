var app = angular.module('testApp', []);

app.config(function($interpolateProvider, $locationProvider) {
	$interpolateProvider.startSymbol('[[');
	$interpolateProvider.endSymbol(']]');
	$locationProvider.html5Mode(true);
});

app.controller("TestController", function($scope) {

	$scope.test = "hello";

});

app.controller("LocationController", function($scope, $location) {
	$scope.$location = {};
	angular.forEach("protocol host port path search hash".split(" "), function(method){
		$scope.$location[method] = function(){
			var result = $location[method].call($location);
			return angular.isObject(result) ? angular.toJson(result) : result;
		};
	});

	$scope.test = "working";
});
