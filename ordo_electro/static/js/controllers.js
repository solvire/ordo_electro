/**
 * INSPINIA - Responsive Admin Theme
 * Copyright 2015 Webapplayers.com
 *
 */

/**
 * MainCtrl - controller
 */
function MainCtrl() {

    this.userName = 'Example user';
    this.helloText = 'Welcome in SeedProject';
    this.descriptionText = 'It is an application skeleton for a typical AngularJS web app. You can use it to quickly bootstrap your angular webapp projects and dev environment for these projects.';

};

/**
 * SocialAccountsCtrl - Social User Accounts 
 * used all over the place probably 
 * sets the dominant account for a screen 
 */
function SocialAccountsCtrl($scope, $http) {
	
	$scope.socialAccounts = [];
	
	// activeSocialAccount --- stores the holder 
	$http({
		method : 'GET',
		url : '/social/accounts/'
	}).success(function(result) {
		$scope.socialAccounts = result;
	});

}

/**
 * twitter specific stuff 
 * @param $scope
 * @param $http
 */
function TwitterAccountsCtrl($scope, $http) {
	$scope.twitterAccounts = [];
	
	// activeSocialAccount --- stores the holder 
	$http({
		method : 'GET',
		url : '/social/accounts/'
	}).success(function(result) {
		$scope.socialAccounts = result;
	});

	
}


angular
    .module('inspinia')
    .controller('MainCtrl', MainCtrl)
    .controller('SocialAccountsCtrl', SocialAccountsCtrl)
    .controller('TwitterAccountsCtrl', TwitterAccountsCtrl)
    
