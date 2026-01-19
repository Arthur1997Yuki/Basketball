import PointsEarned 
import FastBreakFlag
import OffTurnoverFlag


class Result:

    is_success : bool
    points_earned : PointsEarned
    is_fast_break_flag : FastBreakFlag
    is_off_turnover_flag : OffTurnoverFlag
    
    def __init__(self, is_success, points_earned, is_fast_break_flag, is_off_turnover_flag):
        
        self.is_success = is_success
        self.points_earned = points_earned
        self.is_fast_break_flag = is_fast_break_flag
        self.is_off_turnover_flag = is_off_turnover_flag