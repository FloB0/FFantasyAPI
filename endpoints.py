GET_ENDPOINTS = {
    'league_standings': '/leagues/{leagueId}/standings',
    'league_standings_for_game': '/games/{gameId}/leagues/{leagueId}/standings',
    'league_season_stats': '/leagues/{leagueId}/seasonstats',
    'league_stats_for_game': '/games/{gameId}/leagues/{leagueId}/seasonstats'
    # ... other GET endpoints ...
}

POST_ENDPOINTS = {
    'create_league': 'leagues/create',
    'submit_game_score': 'games/{gameId}/submit_score',
    # ... other POST endpoints ...
}