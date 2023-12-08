from bs4 import BeautifulSoup

html_code = """
<div id="refreshOrderHistory" style="height: 472px;">					
                    <table class="adminform table_sort" data-sort="sort_table" id="table_sort_1">
                        <thead>
                        <tr style="position: sticky;top: 0;">
                            <th style="text-align:center;" id="dateadded" onclick="Sort()" title="Date by ascending or descending"><button type="button" id="sort_button">Date Added ▼</button></th>
                            <!--<th width="5%">C/N</th>
                            <th width="5%">W/N</th>
                            <th width="5%">DM/N</th>-->
                            <th style="text-align:center;">Status</th>
                            <th style="text-align:center;">User name</th>
                            <th style="text-align:center;">Comment</th>
                        </tr>
                         </thead>
                        <tbody>
                                                    <tr class="tr">
                                <td style="white-space:nowrap"><span id="date_added">2023-12-06 15:10:36</span></td>
                    <td style="text-align:center;"><strong>Paid Partial Info</strong>
                        <br><span id="cn" title="Customer Notified"> c/n </span>
                        <span id="wn" title="Warehouse Notified"></span>
                        <span id="dmn" title="Driver Manager Notified"></span>
                    </td>
                    <td>jasneet.lakhyan@gmail.com</td>
                     <td style="text-align:left;word-break: break-word;">From frontend |  Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.1 Mobile/15E148 Safari/604.1 | beanstream(117681989)<div style="display:none;" class="history_168331072"></div>
                                            </td>
                    <!--<td style="text-align:center;"><img src="https://adm.bloomex.ca/administrator/images/tick.png"/></td>
                    <td style="text-align:center;"><img src="https://adm.bloomex.ca/administrator/images/publish_x.png"/></td>
                    <td style="text-align:center;"><img src="https://adm.bloomex.ca/administrator/images/publish_x.png"/></td>-->
                            </tr>
                                                        <tr class="tr">
                                <td style="white-space:nowrap"><span id="date_added">2023-12-06 15:21:18</span></td>
                    <td style="text-align:center;"><strong>Paid</strong>
                        <br><span id="cn" title="Customer Notified"></span>
                        <span id="wn" title="Warehouse Notified"></span>
                        <span id="dmn" title="Driver Manager Notified"></span>
                    </td>
                    <td>jasneet.lakhyan@gmail.com</td>
                     <td style="text-align:left;word-break: break-word;">Pending Delivery Address -&gt; Paid<div style="display:none;" class="history_168331325"></div>
                                            </td>
                    <!--<td style="text-align:center;"><img src="https://adm.bloomex.ca/administrator/images/publish_x.png"/></td>
                    <td style="text-align:center;"><img src="https://adm.bloomex.ca/administrator/images/publish_x.png"/></td>
                    <td style="text-align:center;"><img src="https://adm.bloomex.ca/administrator/images/publish_x.png"/></td>-->
                            </tr>
                                                        <tr class="tr">
                                <td style="white-space:nowrap"><span id="date_added">2023-12-06 15:22:05</span></td>
                    <td style="text-align:center;"><strong>Confirmed</strong>
                        <br><span id="cn" title="Customer Notified"> c/n </span>
                        <span id="wn" title="Warehouse Notified"></span>
                        <span id="dmn" title="Driver Manager Notified"></span>
                    </td>
                    <td>vancouver3@bloomex.ca</td>
                     <td style="text-align:left;word-break: break-word;"> <div style="display:none;" class="history_168331340"></div>
                                            </td>
                    <!--<td style="text-align:center;"><img src="https://adm.bloomex.ca/administrator/images/tick.png"/></td>
                    <td style="text-align:center;"><img src="https://adm.bloomex.ca/administrator/images/publish_x.png"/></td>
                    <td style="text-align:center;"><img src="https://adm.bloomex.ca/administrator/images/publish_x.png"/></td>-->
                            </tr>
                                                        <tr class="tr">
                                <td style="white-space:nowrap"><span id="date_added">2023-12-06 15:22:26</span></td>
                    <td style="text-align:center;"><strong>Paid</strong>
                        <br><span id="cn" title="Customer Notified"></span>
                        <span id="wn" title="Warehouse Notified"></span>
                        <span id="dmn" title="Driver Manager Notified"></span>
                    </td>
                    <td>vancouver4@bloomex.ca</td>
                     <td style="text-align:left;word-break: break-word;">resend delivery system and cancel old deliveries<div style="display:none;" class="history_168331345"></div>
                                            </td>
                    <!--<td style="text-align:center;"><img src="https://adm.bloomex.ca/administrator/images/publish_x.png"/></td>
                    <td style="text-align:center;"><img src="https://adm.bloomex.ca/administrator/images/publish_x.png"/></td>
                    <td style="text-align:center;"><img src="https://adm.bloomex.ca/administrator/images/publish_x.png"/></td>-->
                            </tr>
                                                        <tr class="tr">
                                <td style="white-space:nowrap"><span id="date_added">2023-12-06 15:22:32</span></td>
                    <td style="text-align:center;"><strong>In Packaging</strong>
                        <br><span id="cn" title="Customer Notified"></span>
                        <span id="wn" title="Warehouse Notified"></span>
                        <span id="dmn" title="Driver Manager Notified"></span>
                    </td>
                    <td>vancouver4@bloomex.ca</td>
                     <td style="text-align:left;word-break: break-word;">PIN: 334448673072<div style="display:none;" class="history_168331346"></div>
                                            </td>
                    <!--<td style="text-align:center;"><img src="https://adm.bloomex.ca/administrator/images/publish_x.png"/></td>
                    <td style="text-align:center;"><img src="https://adm.bloomex.ca/administrator/images/publish_x.png"/></td>
                    <td style="text-align:center;"><img src="https://adm.bloomex.ca/administrator/images/publish_x.png"/></td>-->
                            </tr>
                                                        <tr class="tr">
                                <td style="white-space:nowrap"><span id="date_added">2023-12-06 15:27:44</span></td>
                    <td style="text-align:center;"><strong>In Packaging</strong>
                        <br><span id="cn" title="Customer Notified"></span>
                        <span id="wn" title="Warehouse Notified"></span>
                        <span id="dmn" title="Driver Manager Notified"></span>
                    </td>
                    <td>tamta.shengelia@bloomex.ca</td>
                     <td style="text-align:left;word-break: break-word;">cust called to confirm that her card message will be printed on card/ ph <div style="display:none;" class="history_168331452"></div>
                                            </td>
                    <!--<td style="text-align:center;"><img src="https://adm.bloomex.ca/administrator/images/publish_x.png"/></td>
                    <td style="text-align:center;"><img src="https://adm.bloomex.ca/administrator/images/publish_x.png"/></td>
                    <td style="text-align:center;"><img src="https://adm.bloomex.ca/administrator/images/publish_x.png"/></td>-->
                            </tr>
                                                        <tr class="tr">
                                <td style="white-space:nowrap"><span id="date_added">2023-12-06 17:23:56</span></td>
                    <td style="text-align:center;"><strong>in transit</strong>
                        <br><span id="cn" title="Customer Notified"> c/n </span>
                        <span id="wn" title="Warehouse Notified"></span>
                        <span id="dmn" title="Driver Manager Notified"></span>
                    </td>
                    <td>vancouver3@bloomex.ca</td>
                     <td style="text-align:left;word-break: break-word;"><b>Warehouse : </b>Vancouver<br><b>Courier info : </b>telephone_or_email[--1--]Call 1(888)744-7123 or www.purolator.com - enter tracking number<br><b>Tracking number : </b>334448673072<div style="display:none;" class="history_168333147"></div>
                                            </td>
                    <!--<td style="text-align:center;"><img src="https://adm.bloomex.ca/administrator/images/tick.png"/></td>
                    <td style="text-align:center;"><img src="https://adm.bloomex.ca/administrator/images/publish_x.png"/></td>
                    <td style="text-align:center;"><img src="https://adm.bloomex.ca/administrator/images/publish_x.png"/></td>-->
                            </tr>
                                                        <tr class="tr">
                                <td style="white-space:nowrap"><span id="date_added">2023-12-07 23:10:01</span></td>
                    <td style="text-align:center;"><strong>Delivered</strong>
                        <br><span id="cn" title="Customer Notified"></span>
                        <span id="wn" title="Warehouse Notified"></span>
                        <span id="dmn" title="Driver Manager Notified"></span>
                    </td>
                    <td>Cron Bot</td>
                     <td style="text-align:left;word-break: break-word;">Cron Update Status to Delivered<div style="display:none;" class="history_168349986"></div>
                                            </td>
                    <!--<td style="text-align:center;"><img src="https://adm.bloomex.ca/administrator/images/publish_x.png"/></td>
                    <td style="text-align:center;"><img src="https://adm.bloomex.ca/administrator/images/publish_x.png"/></td>
                    <td style="text-align:center;"><img src="https://adm.bloomex.ca/administrator/images/publish_x.png"/></td>-->
                            </tr>
                                                    </tbody>
                    </table>
                </div>

"""

# Создаем объект BeautifulSoup
soup = BeautifulSoup(html_code, 'html.parser')

# Находим все комментарии с помощью CSS-селектора
comments = soup.select('td[style="text-align:left;word-break: break-word;"]')

# Извлекаем и выводим текст из каждого комментария
for comment in comments:
    text = comment.get_text(strip=True)
    if text:
        print(text)
