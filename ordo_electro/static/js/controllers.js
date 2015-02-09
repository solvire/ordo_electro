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
 * used all over the place 
 */
function socialAccountsCtrl($scope, $http) {
	$scope.socialAccounts = [];

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
    .controller('socialAccountsCtrl', socialAccountsCtrl)