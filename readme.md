### Description:
A restaurant chain has reached out to your team to build a reservation system.
Here are the details:

Two categories of users / customers: guest user or registered user.
Users should be able to search for a table and reserve.
o	User doesn’t need to login to the system to reserve a table. If registered users, they can login.
o	User enters name, phone, email, date and time (date picker), and # of guests for dining and system presents available tables.
o	Tables have maximum capacity limit i.e., 2, 4, 6, or 8.
o	Different combinations are allowed, and owner accommodates the seating, for example: someone requests 8 guests and table for 8 is not available but 2 + 6, or 4+4 is available. System should combine the tables and notify owner they need to combine tables. In this case System reserves both tables.
If a guest user i.e., not a registered user, system should prompt user to register (Optional) before finalizing the reservation.
Registered users will have these fields:
o	Name, mailing address, billing address (checkbox if same as mailing address), Preferred Diner # (system generated), Earned points (based on $ spent i.e., $1 is 1 point), preferred payment method (cash, credit, check).
System should track high traffic days / weekends and a hold fee is required i.e. July 4th will require valid credit card on system to reserve the table.
o	Notify user no show will have minimum $10 charge.

### 描述。
一家连锁餐厅向你的团队伸出援手，希望建立一个预订系统。
以下是细节。

两类用户/客户：客人用户或注册用户。
用户应该能够搜索到一个桌子并预订。
o 用户不需要登录系统来预订桌子。如果是注册用户，他们可以登录。
o 用户输入姓名、电话、电子邮件、日期和时间（日期选择器），以及用餐的客人数量，系统就会显示可用的桌子。
o 桌子有最大容量限制，即2、4、6或8。
o 允许不同的组合，业主容纳座位，例如：有人要求8位客人，8位的桌子没有，但2+6，或4+4有。系统应该合并这些桌子，并通知业主他们需要合并桌子。在这种情况下，系统保留这两张桌子。
如果是客人用户，即不是注册用户，系统应提示用户在最终确定预订前注册（可选）。
注册用户将有这些字段。
姓名、邮寄地址、帐单地址（如果与邮寄地址相同，请勾选）、首选餐厅#（系统生成）、赚取的积分（基于花费的美元，即1美元为1分）、首选支付方式（现金、信用卡、支票）。
系统应该跟踪高流量的日子/周末，并且需要保留费用，例如，7月4日需要在系统上使用有效的信用卡来保留桌子。
o 通知用户不出现将有最低10美元的费用。

### Note
I ran the server in Docker, so you may now view the website from anywhere by entering the IP address.

http://43.142.169.51:8000/

