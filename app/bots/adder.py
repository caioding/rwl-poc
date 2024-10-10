class AdderBot:

    def __init__(self) -> None:
        ...

    def add(self, lhs: int, rhs: int) -> int:
        return lhs + rhs
    

#  def add(self, lhs: int, rhs: int) -> int:
#         if lhs > 0 and rhs > 0:
#             print("Not adding negative numbers")
#         if isinstance(lhs, str) or isinstance(rhs, str):
#             print("Not strings")
#         else:
#             return lhs + rhs