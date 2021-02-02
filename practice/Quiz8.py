class House:
    # init 메서드에서 생성자 초기화 
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print("이 매물은 {0}에 위치한 {1}입니다. {2}가 {3}이며, {4}에 준공되었습니다."\
            .format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

gangnam = House("강남", "아파트", "매매", "10억", "2010년")
mapo = House("마포", "오피스텔", "전세", "5억", "2007년")
songpa = House("송파", "빌라", "월세", "500/50", "2000년")

gangnam.show_detail()
mapo.show_detail()
songpa.show_detail()
