from dataclasses import dataclass
from backend.Models.Seasons.Season import Season
from backend.Models.TeamAffiliations.Division import Division
from backend.Models.TeamAffiliations.ConferenceName import Conference


@dataclass(frozen=True)
class TeamAffiliation:

    division : Division
    conference : Conference
    season : Season

    def __post_init__(self):
        if not isinstance(self.division, Division):
            raise TypeError("division must be an instance of Division")
        if not isinstance(self.conference, Conference):
            raise TypeError("conference must be an instance of Conference")
        if not isinstance(self.season, Season):
            raise TypeError("season must be an instance of Season")
        
        #ディビジョンがデータベースに存在しない場合はエラー
        

        #カンファレンスがデータベースに存在しない場合はエラー


        #シーズンがデータベースに存在しない場合はエラー