from . import analyse_start, analyse_end, analyse_path, timeLine, orderLine ,weatherBar

if __name__ == "__main__":
    analyse_start.start_analyse("D:\BigData\order_20161101","../static/start.json")
    analyse_end.end_analyse("D:\BigData\order_20161101", "../static/end.json")
    analyse_path.path_analyse("D:\BigData\gps_20161101","../static/gps.json")


    s1 = timeLine.analyse_time("D:\BigData\order_20161101")
    s2 = timeLine.analyse_time("D:\BigData\order_20161105")
    timeLine.draw(s1,s2,"../templates/timeLine.html")

    dis_list = orderLine.orderBarData("D:\BigData\order_20161101")
    bar = orderLine.draw(dis_list)
    bar.render("../templates/orderLine.html")

    d1 = weatherBar.analyse("D:\BigData\order_20161101")
    d2 = weatherBar.analyse("D:\BigData\order_20161108")
    d3 = weatherBar.analyse("D:\BigData\order_20161122")
    weatherBar.draw(d1,d2,d3, "../templates/weatherBar.html")