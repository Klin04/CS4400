import pymysql.cursors
import base64

mydb = pymysql.connect(
    host="localhost",
    user="root",
    passwd="Lkj!19990424",
    database="project3",
    cursorclass=pymysql.cursors.DictCursor
)


def Login(Email, Password):
    with mydb as mycursor:
        # encrypted_password = str(base64.b64encode(Password.encode()))
        mycursor.execute("Select * from emails where email = %s", (Email,))
        myResult = mycursor.fetchone()
        if not myResult:
            return None
        mycursor.execute("Select * from users where username = %s and pass_word = %s",
                         (myResult['username'], Password,))
        myFinalResult = mycursor.fetchone()
        if myFinalResult:
            return myFinalResult
        return None


def SearchEmployeeType(Username):
    with mydb as mycursor:
        mycursor.execute("Select * from employees where username = %s", (Username,))
        myresult = mycursor.fetchone()
        return myresult


def RegisterUser(Fname, Lname, Username, Password, Emails):
    with mydb as mycursor:
        arguments = (Username, Password, 'pending', Fname, Lname, 0, 0,)
        mycursor.execute(
            "insert into users (username, pass_word, user_status, fname, lname, is_employee, is_visitor) values (%s, %s, %s, %s, %s, %s, %s)",
            arguments)
        for email in Emails:
            print(mycursor.execute("insert into emails(username, email) values (%s, %s)", (Username, email)))


def RegisterVisitor(Fname, Lname, Username, Password, Emails):
    with mydb as mycursor:
        arguments = (Username, Password, 'pending', Fname, Lname, 0, 1,)
        mycursor.execute(
            "insert into users (username, pass_word, user_status, fname, lname, is_employee, is_visitor) values (%s, %s, %s, %s, %s, %s, %s)",
            arguments)
        for email in Emails:
            mycursor.execute("insert into emails(username, email) values (%s, %s)", (Username, email))


def RegisterEmployee(Fname, Lname, Username, Password, Emails, EmployeeId, Phone, Address, City, State, Zipcode, Erole):
    with mydb as mycursor:
        arguments = (Username, Password, 'pending', Fname, Lname, 1, 0,)
        mycursor.execute(
            "insert into users (username, pass_word, user_status, fname, lname, is_employee, is_visitor) values (%s, %s, %s, %s, %s, %s, %s)",
            arguments)
        for email in Emails:
            mycursor.execute("insert into emails(username, email) values (%s, %s)", (Username, email))
        arguments = (Username, EmployeeId, Phone, Address, City, State, Zipcode, Erole,)
        mycursor.execute(
            "insert into employees(username, employee_id, phone, address, city, state, zipcode, erole) values (%s, %s, %s, %s, %s, %s, %s, %s)",
            arguments)


def RegisterEmployeeVisitor(Fname, Lname, Username, Password, Emails, EmployeeId, Phone, Address, City, State, Zipcode,
                            Erole):
    with mydb as mycursor:
        arguments = (Username, Password, 'pending', Fname, Lname, 1, 1,)
        mycursor.execute(
            "insert into users (username, pass_word, user_status, fname, lname, is_employee, is_visitor) values (%s, %s, %s, %s, %s, %s, %s)",
            arguments)
        for email in Emails:
            mycursor.execute("insert into emails(username, email) values (%s, %s)", (Username, email))
        arguments = (Username, EmployeeId, Phone, Address, City, State, Zipcode, Erole,)
        mycursor.execute(
            "insert into employees(username, employee_id, phone, address, city, state, zipcode, erole) values (%s, %s, %s, %s, %s, %s, %s, %s)",
            arguments)


def IsEmailUnique(email):
    with mydb as mycursor:
        mycursor.execute("select * from emails where email = %s", email)
        some_email = mycursor.fetchone()
        if some_email:
            return False
        else:
            return True


def IsPhoneUnique(phone):
    with mydb as mycursor:
        mycursor.execute("select * from employees where phone = %s", phone)
        any_phone = mycursor.fetchone()
        if any_phone:
            return False
        else:
            return True


def IsUsernameUnique(username):
    with mydb as mycursor:
        mycursor.execute("select * from users where username = %s", username)
        any_user = mycursor.fetchone()
        if any_user:
            return False
        else:
            return True


def IsEmployeeIdUnique(username):
    with mydb as mycursor:
        mycursor.execute("select * from employees where username = %s", username)
        any_user = mycursor.fetchone()
        if any_user:
            return False
        else:
            return True


def AddEmailForUsername(email, username):
    with mydb as mycursor:
        mycursor.execute("insert into emails(username, email) values (%s, %s)", (username, email))


def GetAllTransportTypeFromTransits():
    """
    For Screen 15/22 drop down menu for Transport Type
    :return: list of transport
    """
    with mydb as mycursor:
        mycursor.execute("select distinct transit_type from transits")
        return mycursor.fetchall()


def GetAllSiteNameFromConnect():
    """
    For Screen 15/22/23 drop down menu for Contain Site
    :return: list
    """
    with mydb as mycursor:
        mycursor.execute("select distinct connect_name from connect")
        return mycursor.fetchall()


def GetAllRoutesWithSitename(sitename):
    with mydb as mycursor:
        mycursor.execute("select transit_type, transit_route , price, count(*) as connected_sites from connect, "
                         "(select transit_type, transit_route , price from transits where transit_type in (select "
                         "connect_type from connect where connect_name = %s) and transit_route in (select "
                         "connect_route from connect where connect_name =  %s)) as temp where "
                         "connect.connect_type = temp.transit_type  and connect.connect_route = temp.transit_route "
                         "group by transit_type , transit_route", (sitename, sitename,))
        return mycursor.fetchall()


def GetAllRoutesWithTransportType(transit_type):
    with mydb as mycursor:
        mycursor.execute("select transit_type, transit_route, price, count(*) as connected_sites from connect, "
                         "(select transit_type, transit_route , price from transits "
                         "where transit_type = %s) as temp where connect.connect_type = temp.transit_type "
                         "and connect.connect_route = temp.transit_route group by transit_type , transit_route",
                         transit_type)
        return mycursor.fetchall()


def GetAllRoutesWithPriceRange(low_price, high_price):
    with mydb as mycursor:
        mycursor.execute("select transit_type, transit_route , price, count(*) as connected_sites from connect, "
                         "(select transit_type, transit_route , price from transits where price "
                         "BETWEEN %s And %s) as temp where connect.connect_type = temp.transit_type "
                         "and connect.connect_route = temp.transit_route group by transit_type , transit_route",
                         (low_price, high_price,))
        return mycursor.fetchall()


def GetAllRoutes():
    with mydb as mycursor:
        mycursor.execute("select transit_type, transit_route , price, count(*) as connected_sites from connect, "
                         "(select transit_type, transit_route , price from transits) as temp "
                         "where connect.connect_type = temp.transit_type "
                         "and connect.connect_route = temp.transit_route "
                         "group by transit_type , transit_route")
        return mycursor.fetchall()


def GetAllRoutesForTakeTransit(transit_type, sitename, low_price, high_price):
    """
    Filters all the routes for taking transits, for Screen 15
    :return: list of routes and their information
    """
    list_of_all_routes = GetAllRoutes()
    if transit_type is not None:
        list_of_routes_filtered_by_transport_type = GetAllRoutesWithTransportType(transit_type)
        # do intersection
        list_of_all_routes = [i for n, i in enumerate(list_of_all_routes) if
                              i in list_of_routes_filtered_by_transport_type]
    if sitename is not None:
        list_of_routes_filtered_by_sitename = GetAllRoutesWithSitename(sitename)
        # do intersection
        list_of_all_routes = [i for n, i in enumerate(list_of_all_routes) if
                              i in list_of_routes_filtered_by_sitename]
    if low_price is not None and high_price is not None:
        list_of_routes_filtered_by_price_range = GetAllRoutesWithPriceRange(low_price, high_price)
        # do intersection
        list_of_all_routes = [i for n, i in enumerate(list_of_all_routes) if
                              i in list_of_routes_filtered_by_price_range]
    return list_of_all_routes


def GetCurrentSiteManagerAndAllUnAssignedManagers(sitename):
    """
    For screen 20, shows a 'dropdown list containing the current site manager as well
    as the managers who have not yet been assigned to another site'
    :param sitename: the current site name
    :return:
    """
    with mydb as mycursor:
        mycursor.execute(
            "select distinct (fname, lname) as name from users where username in "
            "(select distinct username from employees where employee_id in (select sitemanager_id from sites where sitename = %s)) "
            "union (select username from employees where employee_id not in (select sitemanager_id from sites))",
            sitename)
        return mycursor.fetchall()


def UpdateSiteInformation(sitename, zipcode, address, openeveryday, sitemanager_id, new_sitename):
    """
    Used for screen 20, edits the site information by administrator
    :param sitename:
    :param zipcode:
    :param address:
    :param openeveryday:
    :param sitemanager_id:
    :return:
    """
    with mydb as mycursor:
        arguments = (zipcode, address, openeveryday, sitemanager_id, sitename,)
        mycursor.execute(
            "update sites SET zipcode = %s, address = %s, openeveryday = %s, sitemanager_id = %s WHERE sitename = %s",
            arguments)
        mycursor.execute("update sites set sitename = %s where sitename = %s", (new_sitename, sitename))


def GetManagersNotAssignedSite():
    """
    For screen 21, where we need a drop down list of all the managers not assigned to a site
    :return: list
    """
    with mydb as mycursor:
        mycursor.execute("select fname, lname from users where username in "
                         "(select distinct username from employees where employee_id not in (select sitemanager_id from sites))")
        return mycursor.fetchall()


def GetEmployeeInformation():
    # TODO: this
    with mydb as mycursor:
        # mycursor.execute("select fname, lname from users where username in "
        #                  "(select distinct username from employees where employee_id not in (select sitemanager_id from sites))")
        return mycursor.fetchall()


def UpdateUserInformation(username, fname, lname, is_visitor, phone, employee_id):
    with mydb as mycursor:
        mycursor.execute("update users set fname = %s, lname = %s, is_visitor = %s where username = %s",
                         (fname, lname, is_visitor, username))
        mycursor.execute("update employee set phone = %s where employee_id = %s", (phone, employee_id))


def AddAllEmailsOfAUser(emails, username):
    with mydb as mycursor:
        for email in emails:
            mycursor.execute("insert into emails(username, email) values (%s, %s)", (username, email))


def RemoveAllEmailsOfAUser(username):
    with mydb as mycursor:
        mycursor.execute("delete from emails where username = %s)", username)


def AddNewSites(sitename, zipcode, address, openeveryday, sitemanager_id):
    """
    Adds a new site, note that if there is NO ADDRESS, please pass in None
    :param sitename:
    :param zipcode:
    :param address: None if no address is supplied
    :param openeveryday:
    :param sitemanager_id:
    :return:
    """
    with mydb as mycursor:
        mycursor.execute(
            "insert into sites(sitename, zipcode, address, openeveryday, sitemanager_id) values (%s, %s, %s, %s, %s)",
            (sitename, zipcode, address, openeveryday, sitemanager_id,))


def UpdateTransitPriceAndRoute(price, transit_type, old_transit_route, new_transit_route):
    """
    For screen 23, editing the price and the transit route
    :param price:
    :param transit_type:
    :param old_transit_route:
    :param new_transit_route:
    :return:
    """
    with mydb as mycursor:
        # first update price
        mycursor.execute(
            "UPDATE transits SET price = %s WHERE transit_type = %s and transit_route = %s",
            (price, transit_type, old_transit_route))
        # update route
        mycursor.execute(
            "update transits set transit_route = %s where transit_type = %s, transit_route = %s",
            (new_transit_route, transit_type, old_transit_route))


def UpdateTransitAddSites(connect_type, connect_route, connect_name):
    """
    add new sites to the transit (connected sites)
    :param connect_type:
    :param connect_route:
    :param connect_name:
    :return:
    """
    with mydb as mycursor:
        # add new sites to this transit
        mycursor.execute(
            "insert into connect (connect_type, connect_route, connect_name) values (%s, %s, %s)",
            (connect_type, connect_route, connect_name))


def UpdateTransitDeleteAllSites(connect_type, connect_route):
    """
    delete ALL sites from a transit (PK-> transit_type:connect_type, transit_route:connect_route)
    :param connect_type:
    :param connect_route:
    :return:
    """
    with mydb as mycursor:
        # add new sites to this transit
        mycursor.execute(
            "delete from connect where connect_type = %s and connect_route = %s",
            (connect_type, connect_route))


def GetAllSites():
    """
    returns all the distinct sitenames
    :return:
    """
    with mydb as mycursor:
        mycursor.execute("select distinct sitename from sites")
        return mycursor.fetchall()


def AddTransit(transit_type, transit_route, price):
    """
    IMPORTANT BEFORE YOU USE THIS METHOD, price is NONE negative and also REMEMBER to call AddNewSites for all the sites
    for this transit!!!
    for screen 24, administrator creates new transit
    :param transit_type:
    :param transit_route:
    :param price:
    :return:
    """
    with mydb as mycursor:
        mycursor.execute(
            "insert into transits(transit_type, transit_route, price) values (%s, %s, %s)",
            (transit_type, transit_route, price))


def IsSitenameUnique(sitename):
    with mydb as mycursor:
        mycursor.execute("select * from sites where sitename = %s", sitename)
        if mycursor.fetchone():
            return True
        else:
            return False


def DeleteEvent(event_name, sitename, startdate):
    """
    for screen 25, when managers deletes the selected tuples (event)
    :param event_name:
    :param sitename:
    :param startdate:
    :return:
    """
    with mydb as mycursor:
        mycursor.execute(
            "delete from site_events where event_name = %s and sitename = %s and startdate = %s",
            (event_name, sitename, startdate))


def DeleteTransit(transit_type, transit_route):
    """
    Deletes Transit given its PKs -> the two args
    For Screen 22, when admin manage transit
    :param transit_type:
    :param transit_route:
    :return:
    """
    with mydb as mycursor:
        mycursor.execute("delete from transits where transit_type = %s and transit_route = %s",
                         (transit_type, transit_route))


def GetAllEventFilteredByEventName_DescripKeyword_StartDate_EndDate_DurationRange_VisitRange_RevenueRange(
        event_name, keyword, start_date, end_date, duration_range_low, duration_range_high, visit_range_low,
        visit_range_high,
        revenue_range_low, revenue_range_high):
    """
    Screen 25 table, look at this insanely long method name
    i luv it
    :param event_name:
    :param keyword:
    :param start_date:
    :param end_date:
    :param duration_range_low:
    :param duration_range_high:
    :param visit_range_low:
    :param visit_range_high:
    :param revenue_range_low:
    :param revenue_range_high:
    :return:
    """
    with mydb as mycursor:
        # first get ALL result
        mycursor.execute(
            "SELECT event_name, sitename, startdate, endate, duration, staff_count, total_visit, revenue FROM staff_visitor_revenue")
        all_result = mycursor.fetchall()
        if event_name is not None:
            mycursor.execute(
                "SELECT event_name, sitename, startdate, endate, duration, staff_count, total_visit, revenue "
                "FROM staff_visitor_revenue WHERE event_name like concat('%', %s,'%')", event_name)
            filtered_result = mycursor.fetchall()
            all_result = [i for n, i in enumerate(all_result) if i in filtered_result]
        if keyword is not None:
            mycursor.execute(
                "SELECT event_name, sitename, startdate, endate, duration, staff_count, total_visit, revenue "
                "FROM staff_visitor_revenue WHERE event_name like concat('%', %s,'%')", keyword)
            filtered_result = mycursor.fetchall()
            all_result = [i for n, i in enumerate(all_result) if i in filtered_result]
        if start_date is not None:
            mycursor.execute(
                "SELECT event_name, sitename, startdate, endate, duration, staff_count, total_visit, revenue "
                "FROM staff_visitor_revenue WHERE startdate = start", start_date)
            filtered_result = mycursor.fetchall()
            all_result = [i for n, i in enumerate(all_result) if i in filtered_result]
        if end_date is not None:
            mycursor.execute(
                "SELECT event_name, sitename, startdate, endate, duration, staff_count, total_visit, revenue "
                "FROM staff_visitor_revenue WHERE endate = end", end_date)
            filtered_result = mycursor.fetchall()
            all_result = [i for n, i in enumerate(all_result) if i in filtered_result]
        if duration_range_low is not None and duration_range_high is not None:
            mycursor.execute(
                "SELECT event_name, sitename, startdate, endate, duration, staff_count, total_visit, revenue "
                "FROM staff_visitor_revenue WHERE duration between %s and %s",
                (duration_range_low, duration_range_high))
            filtered_result = mycursor.fetchall()
            all_result = [i for n, i in enumerate(all_result) if i in filtered_result]
        if visit_range_low is not None and visit_range_high is not None:
            mycursor.execute(
                "SELECT event_name, sitename, startdate, endate, duration, staff_count, total_visit, revenue "
                "FROM staff_visitor_revenue WHERE total_visit between low and high",
                (visit_range_low, visit_range_high))
            filtered_result = mycursor.fetchall()
            all_result = [i for n, i in enumerate(all_result) if i in filtered_result]
        if revenue_range_low is not None and revenue_range_high is not None:
            mycursor.execute(
                "SELECT event_name, sitename, startdate, endate, duration, staff_count, total_visit, revenue "
                "FROM staff_visitor_revenue WHERE revenue between low and high",
                (revenue_range_low, revenue_range_high))
            filtered_result = mycursor.fetchall()
            all_result = [i for n, i in enumerate(all_result) if i in filtered_result]
        return all_result


def GetTransitByFilterByTransportType_Route_ContainSite_PriceRange(transit_type, route, low_price, high_price):
    """
    Specifically for screen 22, fetching that table, filters the 4 different types of filter,
    If the filter is not applied, please pass in None
    :param transit_type:
    :param route:
    :param low_price:
    :param high_price:
    :return:
    """
    with mydb as mycursor:
        # first get ALL result
        mycursor.execute(
            "select transit_route, transit_type, price, connected_sites, visitors_logged from sites_logged")
        all_result = mycursor.fetchall()

        # Start filtering if this filtering type is applied
        if transit_type is not None:
            mycursor.execute(
                "select transit_route, transit_type, price, connected_sites, visitors_logged from sites_logged "
                "where transit_type = %s", transit_type)
            filtered_result = mycursor.fetchall()
            all_result = [i for n, i in enumerate(all_result) if i in filtered_result]
        if route is not None:
            mycursor.execute(
                "select transit_route, transit_type, price, connected_sites, visitors_logged from sites_logged "
                "where transit_route = %s", route)
            filtered_result = mycursor.fetchall()
            all_result = [i for n, i in enumerate(all_result) if i in filtered_result]
        if low_price is not None and high_price is not None:
            mycursor.execute(
                "select transit_route, transit_type, price, connected_sites, visitors_logged from sites_logged "
                "WHERE price BETWEEN %s AND %s", (low_price, high_price))
            filtered_result = mycursor.fetchall()
            all_result = [i for n, i in enumerate(all_result) if i in filtered_result]
        return all_result


def GetTransitPrice(transit_type, transit_route):
    """
    This method and GetTransitConnectedSites works together to fetch the data needed for
    screen 23
    :param transit_type:
    :param transit_route:
    :return:
    """
    with mydb as mycursor:
        mycursor.execute(
            "select price, connect_name from transits, connect where transit_type = %s and transit_route = %s",
            (transit_type, transit_route))
        return mycursor.fetchone()


def GetTransitConnectedSites(transit_type, transit_route):
    """
    This method and GetTransitPrice works together to fetch the data needed for
    screen 23
    :param transit_type:
    :param transit_route:
    :return:
    """
    with mydb as mycursor:
        mycursor.execute("select connect_name from connect where connect_type = %s and connect_route = %s",
                         (transit_type, transit_route))
        return mycursor.fetchall()


def UserTakeTransitLogNewTransit(take_username, take_type, take_route, take_date):
    """
    Screen 15 log new transit for users for a specific route
    :param take_username:
    :param take_type:
    :param take_route:
    :param take_date:
    :return:
    """
    with mydb as mycursor:
        mycursor.execute("insert into take (take_username, take_type, take_route, take_date) values(%s, %s, %s, %s)",
                         (take_username, take_type, take_route, take_date,))

def GetEventViewEditEventByFilterByVisitRange_RevenueRange(event_name, price, visit_range_high, visit_range_low, revenue_range_low, revenue_range_high):
    pass
    # with mydb as mycursor:
    #     # first get ALL result
    #     mycursor.execute(
    #         "select visit_event_date as date, count(*) as daily_visits, count(*) * %s as daily_revenue "
    #         "from visit_event join site_events on visit_event_name = site_events.event_name "
    #         "and site_events.startdate = visit_event_startdate where visit_event_name = %s "
    #         "group by visit_event_date", (price, event_name, ))
    #     all_result = mycursor.fetchall()
    #
    #     # Start filtering if this filtering type is applied
    #     if visit_range_high is not None and visit_range_low is not None:
    #         mycursor.execute(
    #             "select visit_event_date as date, count(*) as daily_visits, count(*) * %s as daily_revenue "
    #             "from visit_event join site_events on visit_event_name = site_events.event_name "
    #             "and site_events.startdate = visit_event_startdate where visit_event_name = %s "
    #             "group by visit_event_date having daily_visits between %s and %s",
    #             (price, event_name, visit_range_high, visit_range_low))
    #         filtered_result = mycursor.fetchall()
    #         all_result = [i for n, i in enumerate(all_result) if i in filtered_result]
    #     if revenue_range_low is not None and revenue_range_high is not None:
    #         mycursor.execute(
    #             "select transit_type, transit_route, price, connected_sites, visitors_logged from sites_logged "
    #             "where transit_type = %s", transit_type)
    #         filtered_result = mycursor.fetchall()
    #         all_result = [i for n, i in enumerate(all_result) if i in filtered_result]
    #     if route is not None:
    #         mycursor.execute(
    #             "select transit_type, transit_route, price, connected_sites, visitors_logged from sites_logged "
    #             "where transit_route = %s", route)
    #         filtered_result = mycursor.fetchall()
    #         all_result = [i for n, i in enumerate(all_result) if i in filtered_result]
    #     if low_price is not None and high_price is not None:
    #         mycursor.execute(
    #             "select transit_type, transit_route, price, connected_sites, visitors_logged from sites_logged "
    #             "WHERE price BETWEEN %s AND %s", (low_price, high_price))
    #         filtered_result = mycursor.fetchall()
    #         all_result = [i for n, i in enumerate(all_result) if i in filtered_result]
    #     return all_result