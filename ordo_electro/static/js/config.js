/**
 * INSPINIA - Responsive Admin Theme
 * Copyright 2015 Webapplayers.com
 *
 * Inspinia theme use AngularUI Router to manage routing and views
 * Each view are defined as state.
 * Initial there are written state for all view in theme.
 *
 */
function config($stateProvider, $urlRouterProvider, $ocLazyLoadProvider) {
    $urlRouterProvider.otherwise("/index/main");

    $ocLazyLoadProvider.config({
        // Set to true if you want to see what and when is dynamically loaded
        debug: true
    });

    $stateProvider

        .state('index', {
            abstract: true,
            url: "/index",
            templateUrl: "/static/views/common/content.html",
        })
        .state('index.main', {
            url: "/main",
            templateUrl: "/static/views/main.html",
            data: { pageTitle: 'Example view' }
        })
        .state('index.minor', {
            url: "/minor",
            templateUrl: "/static/views/minor.html",
            data: { pageTitle: 'Example view' }
        })
        .state('twitter', {
            abstract: true,
            url: "/twitter",
            templateUrl: "/static/views/common/content.html",
        })
        .state('twitter.dashboard', {
            url: "/twitter_dashboard",
            templateUrl: "/static/views/twitter/dashboard.html",
            data: { pageTitle: 'Twitter Dashboard' },
        })
        .state('twitter.follower_matrix', {
            url: "/follower_matrix",
            templateUrl: "/static/views/twitter/follower_matrix.html",
            data: { pageTitle: 'Twitter Follower Matrix' },
        })
        .state('twitter.accounts', {
            url: "/accounts",
            templateUrl: "/static/views/twitter/accounts.html",
            data: { pageTitle: 'Twitter Accounts' },
        })
}
angular
    .module('inspinia')
    .config(config)
    .run(function($rootScope, $state) {
        $rootScope.$state = $state;
    });
