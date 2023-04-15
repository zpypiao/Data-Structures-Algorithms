1、5键键盘的输出
有一个特殊的5键键盘，上面有a，ctrl-c，ctrl-x，ctrl-v，ctrl-a五个键。a键在屏幕上输出一个字母a；ctrl-c将当前选择的字母复制到剪贴板；ctrl-x将当前选择的字母复制到剪贴板，并清空选择的字母；ctrl-v将当前剪贴板里的字母输出到屏幕；ctrl-a选择当前屏幕上的所有字母。注意：
1 剪贴板初始为空，新的内容被复制到剪贴板时会覆盖原来的内容
2 当屏幕上没有字母时，ctrl-a无效
3 当没有选择字母时，ctrl-c和ctrl-x无效
4 当有字母被选择时，a和ctrl-v这两个有输出功能的键会先清空选择的字母，再进行输出

给定一系列键盘输入，输出最终屏幕上字母的数量。

输入描述:
输入为一行，为简化解析，用数字1 2 3 4 5代表a，ctrl-c，ctrl-x，ctrl-v，ctrl-a五个键的输入，数字用空格分隔
输出描述:
输出一个数字，为最终屏幕上字母的数量

示例1：
输入
1 1 1
输出
3
说明
连续键入3个a，故屏幕上字母的长度为3

示例2：
输入
1 1 5 1 5 2 4 4
输出
2
说明
输入两个a后ctrl-a选择这两个a，再输入a时选择的两个a先被清空，所以此时屏幕只有一个a，后续的ctrl-a，ctrl-c选择并复制了这一个a，最后两个ctrl-v在屏幕上输出两个a，故屏幕上字母的长度为2（第一个ctrl-v清空了屏幕上的那个a）

答案：
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        while (in.hasNext()) {
            String totalStr=in.nextLine();
            int count = 0;
        int copyCount = 0;
        int selCount = 0;
        boolean overOp = false;
        for (char op : totalStr.toCharArray()) {
            if (op == '1') {
                //a
                count = selCount > 0 ? 1 : count + 1;
                selCount = 0;
            } else if (op == '2') {
                //复制
                copyCount = selCount;
            } else if (op == '3') {
                //剪切
                count -= selCount;
                copyCount = selCount;
                selCount = 0;
            } else if (op == '4') {
                //粘贴
                count -= selCount;
                selCount = 0;
                count += copyCount;
            } else if (op == '5') {
                //全选
                selCount = count;
            }
        }
        System.out.println(count);
        }
    }
}

2、N进制减法
实现一个基于字符串的N机制的减法。
需要对输入的两个字符串按照给定的N进制进行减法操作，输出正负符号和表示结果的字符串。

输入描述:
输入：三个参数。
第一个参数是整数形式的进制N值，N值范围为大于等于2、小于等于35。
第二个参数为被减数字符串；
第三个参数为减数字符串。有效的字符包括0~9以及小写字母a~z，字符串有效字符个数最大为100个字符，另外还有结尾的\0。
限制：
输入的被减数和减数，除了单独的0以外，不能是以0开头的字符串。
如果输入有异常或计算过程中有异常，此时应当输出-1表示错误。
输出描述:
输出：2个。
其一为减法计算的结果，-1表示出错，0表示结果为整数，1表示结果为负数。
其二为表示结果的字符串。

示例1:
输入
2 11 1
输出
0 10
说明
按二进制计算 11 -1 ，计算正常，0表示符号为正数，结果为10

示例2:
输入
8 07 1
输出
-1
说明
按8进制，检查到减数不符合非0前导的要求，返回结果为-1，没有其他结果内容。

答案：
import java.util.ArrayList;
import java.util.Scanner;
import java.util.TreeSet;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        Integer request = Integer.parseInt(sc.nextLine());
        sc.close();
        TreeSet<Integer> set = new TreeSet<>();
        for (String str : input.split(",")) {
            if (str.contains("-")) {
                String[] split = str.split("-");
                int start = Integer.parseInt(split[0]);
                int end = Integer.parseInt(split[1]);
                for (int i = start; i <= end; i++) {
                    set.add(i);
                }
            } else {
                set.add(Integer.parseInt(str));
            }
        }
        set.remove(request);

        ArrayList<Integer> list = new ArrayList<>(set);
        StringBuilder sb = new StringBuilder();

        Integer start = list.get(0);
        Integer last = start;
        for (int i = 1; i < list.size(); i++) {
            Integer cur = list.get(i);
            if (cur == last + 1) {
                last = cur;
            } else {
                append(sb, start, last);
                start = last = cur;
            }
        }
        append(sb, start, last);
        System.out.println(sb.substring(0, sb.length() - 1));
    }

    private static void append(StringBuilder sb, Integer start, Integer last) {
        if (start.equals(last)) {
            sb.append(last).append(",");
        } else {
            sb.append(start).append("-").append(last).append(",");
        }
    }
}

3、TLV解码
TLV编码是按[Tag Length Value]格式进行编码的，一段码流中的信元用Tag标识，Tag在码流中唯一不重复，Length表示信元Value的长度，Value表示信元的值。
码流以某信元的Tag开头，Tag固定占一个字节，Length固定占两个字节，字节序为小端序。
现给定TLV格式编码的码流，以及需要解码的信元Tag，请输出该信元的Value。
输入码流的16机制字符中，不包括小写字母，且要求输出的16进制字符串中也不要包含小写字母；码流字符串的最大长度不超过50000个字节。

输入描述:
输入的第一行为一个字符串，表示待解码信元的Tag；
输入的第二行为一个字符串，表示待解码的16进制码流，字节之间用空格分隔。
输出描述:
输出一个字符串，表示待解码信元以16进制表示的Value。

示例1：
输入
31
32 01 00 AE 90 02 00 01 02 30 03 00 AB 32 31 31 02 00 32 33 33 01 00 CC
输出
32 33
说明
需要解析的信元的Tag是31，从码流的起始处开始匹配，Tag为32的信元长度为1（01 00，小端序表示为1）；第二个信元的Tag是90，其长度为2；第三个信元的Tag是30，其长度为3；第四个信元的Tag是31，其长度为2（02 00），所以返回长度后面的两个字节即可，即32 33。

答案：
解法一：
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		while (in.hasNextLine()) {// 注意，如果输入是多个测试用例，请通过while循环处理多个测试用例
			String key=in.nextLine();
			String[] arr=in.nextLine().replaceAll("[a-z]", "").split("[ ]");
			String tag="";
			int length;
			String value="";
			for(int i=0;i<arr.length;) {
				tag="";
				length=0;
				value="";
				tag=arr[i];
				length=Integer.valueOf(arr[i+2]+arr[i+1], 16);
				for(int j=1;j<=length;j++) {
					value+=arr[i+2+j]+" ";
				}
				if(key.equals(tag)) {
					System.out.println(value.trim());
				}
//				System.out.println(tag+" "+length+" "+value.trim());
				i=i+2+length+1;
			}
		}




	}
}

4、VLAN资源池
VLAN是一种对局域网设备进行逻辑划分的技术，为了标识不同的VLAN，引入VLAN ID(1-4094之间的整数)的概念。定义一个VLAN ID的资源池(下称VLAN资源池)，资源池中连续的VLAN用开始VLAN-结束VLAN表示，不连续的用单个整数表示，所有的VLAN用英文逗号连接起来。现在有一个VLAN资源池，业务需要从资源池中申请一个VLAN，需要你输出从VLAN资源池中移除申请的VLAN后的资源池。

输入描述:
第一行为字符串格式的VLAN资源池，第二行为业务要申请的VLAN，VLAN的取值范围为[1,4094]之间的整数。
输出描述:
从输入VLAN资源池中移除申请的VLAN后字符串格式的VLAN资源池，输出要求满足题目描述中的格式，并且按照VLAN从小到大升序输出。
如果申请的VLAN不在原VLAN资源池内，输出原VLAN资源池升序排序后的字符串即可。

示例1：
输入
1-5
2
输出
1,3-5
说明
原VLAN资源池中有VLAN 1、2、3、4、5，从资源池中移除2后，剩下VLAN 1、3、4、5，按照题目描述格式并升序后的结果为1,3-5。

示例2：
输入
20-21,15,18,30,5-10
15
输出
5-10,18,20-21,30
说明
原VLAN资源池中有VLAN 5、6、7、8、9、10、15、18、20、21、30，从资源池中移除15后，资源池中剩下的VLAN为  5、6、7、8、9、10、18、20、21、30，按照题目描述格式并升序后的结果为5-10,18,20-21,30。

示例3：
输入
5,1-3
10
输出
1-3,5
说明
原VLAN资源池中有VLAN 1、2、3，5，申请的VLAN 10不在原资源池中，将原资源池按照题目描述格式并按升序排序后输出的结果为1-3,5。
备注:
输入VLAN资源池中VLAN的数量取值范围为[2-4094]间的整数，资源池中VLAN不重复且合法([1,4094]之间的整数)，输入是乱序的。

答案：
解法一：
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = null;
        int[] vlan = new int[4094];
        try {
            str = br.readLine();
            int num = Integer.parseInt(br.readLine());
            String[] split = str.split(",");
            for (String s : split) {
                try {
                    int index = Integer.parseInt(s);
                    if (index == num) continue;
                    vlan[index] = 1;
                } catch (NumberFormatException exception) {
                    if (s.contains("-")) {
                        String[] s_s = s.split("-");
                        int first = Integer.parseInt(s_s[0]);
                        int end = Integer.parseInt(s_s[1]);
                        for (int i = first; i <= end; i++) {
                            if (num != i) {
                                vlan[i] = 1;
                            }
                        }
                    }
                }
            }
            StringBuilder result = new StringBuilder();
            for (int i = 1; i < vlan.length; i++) {
                if (vlan[i] == 1) {
                    result.append(",");
                    result.append(i);
                    if (++i < vlan.length && vlan[i] == 1) {
                        result.append("-");
                        while (vlan[++i] == 1) {

                        }
                        result.append(i - 1);
                    }
                }
            }
            String resultStr = result.toString();
            if (result.indexOf(",") == 0) {
                resultStr = resultStr.substring(1);
            }
            System.out.println(resultStr);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}

解法二：
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s = in.nextLine();
        String[] array = s.split(",");
        Set<Integer> set = new HashSet();
        for (int i = 0; i < array.length; i++) {
            if (array[i].length() == 0) {
                continue;
            }
            String[] tempArray = array[i].split("-");
            if (tempArray.length == 2) {
                for (int j = Integer.valueOf(tempArray[0]); j <= Integer.valueOf(tempArray[1]); j++) {
                    set.add(j);
                }
            }else{
                set.add(Integer.valueOf(tempArray[0]));
            }
        }
        String filter = in.nextLine();
        set.remove(Integer.valueOf(filter));
        List<Integer> list = new ArrayList(set);
        if (list.size() == 1) {
            System.out.println(list.get(0));
            return;
        }
        Collections.sort(list);
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < list.size()-1; i++) {
            if (list.get(i) == list.get(i + 1) - 1) {
                result.append(","+list.get(i));
                while (i<list.size()-1&&list.get(i) == list.get(i + 1) - 1) {
                    i++;
                }
                result.append("-" + list.get(i));
            }else{
                result.append("," + list.get(i));
            }
            if (i == list.size() - 2) {
                result.append("," + list.get(i + 1));
            }
        }
        String resultString = result.toString();
        if (resultString.length()>0&&resultString.charAt(0) == ',') {
            resultString=resultString.substring(1);
        }
        System.out.println(resultString);
    }
}

5、按身高和体重排队
某学校举行运动会，学生们按编号(1、2、3…n)进行标识，现需要按照身高由低到高排列，对身高相同的人，按体重由轻到重排列；对于身高体重都相同的人，维持原有的编号顺序关系。请输出排列后的学生编号。

输入描述:
两个序列，每个序列由n个正整数组成（0 < n <= 100）。第一个序列中的数值代表身高，第二个序列中的数值代表体重。
输出描述:
排列结果，每个数值都是原始序列中的学生编号，编号从1开始

示例1：
输入
4
100 100 120 130
40 30 60 50
输出
2 1 3 4
说明
输出的第一个数字2表示此人原始编号为2，即身高为100，体重为30的这个人。由于他和编号为1的人身高一样，但体重更轻，因此要排在1前面。

示例2：
输入
3
90 110 90
45 60 45
输出
1 3 2
说明
1和3的身高体重都相同，需要按照原有位置关系让1排在3前面，而不是3 1 2

答案：
解法一：
import java.util.Arrays;
import java.util.Scanner;

public class Main {

    static class Node implements Comparable<Node>{
        int i;
        int h;
        int w;
        Node(int i,int h,int w){
            this.i = i ;
            this.h = h ;
            this.w = w ;
        }

        @Override
        public int compareTo(Node o){
            if(h != o.h)
                return h - o.h ;
            if(w!= o.w)
                return w - o.w ;
            return i - o.i;
        }
    }

    public static void main(String[] args){
        Scanner in = new Scanner(System.in) ;
        while(in.hasNext()){
            int n = in.nextInt() ;
            int [] h = new int [n] ;
            int [] w = new int [n] ;
            for(int i = 0;i < n;i++){
                h[i] = in.nextInt() ;
            }
            for(int i = 0;i < n; i++){
                w[i]= in.nextInt();
            }
            Node[] nodes = new Node [n];
            for(int i = 0;i < n; i++){
                nodes[i] = new Node(i+1,h[i],w[i]);
            }
            Arrays.sort(nodes);
            for(int i =0;i<n;i++){
                System.out.printf("%d%c",nodes[i].i,1 == n-1 ? '\n':' ');
            }
        }
    }
}

6、按索引范围翻转文章片段
输入一个英文文章片段，翻转指定区间的单词顺序，标点符号和普通字母一样处理。例如输入字符串"I am a developer. "，区间[0,3]，则输出"developer. a am I"。

String reverseWords(String s, int start, int end)

输入描述:
使用换行隔开三个参数，第一个参数为英文文章内容即英文字符串，第二个参数为翻转起始单词下标(下标从0开始)，第三个参数为结束单词下标。
输出描述:
翻转后的英文文章片段所有单词之间以一个半角空格分隔进行输出

示例1：
输入
I am a developer.
1
2
输出
I a am developer.
示例2：
输入
  hello world!
0
1
输出
world! hello
说明
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例3：
输入
I am a   developer.
0
3
输出
developer. a am I
说明
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
示例4：
输入
Hello!
0
3
输出
EMPTY
说明
指定翻转区间只有一个单词或无有效单词，则统一输出"EMPTY"

答案：
解法一：
import java.util.ArrayList;
import java.util.Scanner;
import java.util.TreeSet;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        Integer request = Integer.parseInt(sc.nextLine());
        sc.close();
        TreeSet<Integer> set = new TreeSet<>();
        for (String str : input.split(",")) {
            if (str.contains("-")) {
                String[] split = str.split("-");
                int start = Integer.parseInt(split[0]);
                int end = Integer.parseInt(split[1]);
                for (int i = start; i <= end; i++) {
                    set.add(i);
                }
            } else {
                set.add(Integer.parseInt(str));
            }
        }
        set.remove(request);

        ArrayList<Integer> list = new ArrayList<>(set);
        StringBuilder sb = new StringBuilder();

        Integer start = list.get(0);
        Integer last = start;
        for (int i = 1; i < list.size(); i++) {
            Integer cur = list.get(i);
            if (cur == last + 1) {
                last = cur;
            } else {
                append(sb, start, last);
                start = last = cur;
            }
        }
        append(sb, start, last);
        System.out.println(sb.substring(0, sb.length() - 1));
    }

    private static void append(StringBuilder sb, Integer start, Integer last) {
        if (start.equals(last)) {
            sb.append(last).append(",");
        } else {
            sb.append(start).append("-").append(last).append(",");
        }
    }
}

7、报数游戏
100个人围成一圈，每个人有一个编码，编号从1开始到100。他们从1开始依次报数，报到为M的人自动退出圈圈，然后下一个人接着从1开始报数，直到剩余的人数小于M。请问最后剩余的人在原先的编号为多少？

输入描述:
输入一个整数参数M
输出描述:
如果输入参数M小于等于1或者大于等于100，输出“ERROR!”；否则按照原先的编号从小到大的顺序，以英文逗号分割输出编号字符串

示例1：
输入
3
输出
58,91
说明
输入M为3，最后剩下两个人
示例2：
输入
4
输出
34,45,97
说明
输入M为4，最后剩下三个人

答案：
解法一：
import java.util.Scanner;
import java.util.Collections;
import java.util.ArrayList;

public class Main {
    static class node{
        int val;
        node next = null;
        node(int val){this.val=val;}
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int M = in.nextInt();
        if(M<=1||M>=100) System.out.println("ERROR!");
        else{
            ArrayList<Integer> ans = new ArrayList<>();
            node head = new node(1),pre = head;
            for(int i=2;i<=100;i++){
                node now = new node(i);
                pre.next=now;
                pre = now;
            }
            pre.next=head;
            //num记录剩下的人的数量,k记录当前的报数
            int num = 100,k=1;
            while(true){
                k++;
                pre = pre.next;
                head = head.next;
                //如果报数为M，就删除链表的结点
                if(k==M){
                    pre.next=head.next;
                    head=pre.next;
                    k=1;
                    num--;
                }
                if(num<M){
                    pre=head;
                    do{
                        ans.add(head.val);
                        head=head.next;
                    }while(head !=pre);
                    break;
                }
            }
            Collections.sort(ans);
            for(int i=0;i<ans.size();i++){
                System.out.printf("%d%c",ans.get(i),i==ans.size()-1?'\n':',');
            }
        }
    }
}

解法二：
import java.util.*;

public class Main {

    public static void main(String[] args) {
        List<Integer> peopleNos = new ArrayList(100);
        for(int i = 1; i <= 100;i++) {
            peopleNos.add(i);
        }
        Scanner scan = new Scanner(System.in);
        int m = scan.nextInt();
        if (m <= 1 || m >= 100) {
            System.out.println("ERROR!");
            return;
        }
        int num = 0;
        int index = 0;
        while (peopleNos.size() >= m) {
            num++;
            if (index >= peopleNos.size()) {
                index = 0;
            }
            Integer no = peopleNos.get(index);
            if (num == m) {
                //删除该元素，下个元素从1开始报数
                peopleNos.remove(no);
                num = 0;
                index--;
            }
            index++;
        }

        StringBuilder builder = new StringBuilder();
        int count = 0;
        for (Integer i : peopleNos) {
            builder.append(i);
            if (count != peopleNos.size() - 1) {
                builder.append(",");
            }
            count++;
        }
        System.out.println(builder.toString());
    }
}

8、比赛
一个有N个选手参加比赛，选手编号为1~N（3<=N<=100），有M（3<=M<=10）个评委对选手进行打分。打分规则为每个评委对选手打分，最高分10分，最低分1分。
请计算得分最多的3位选手的编号。如果得分相同，则得分高分值最多的选手排名靠前(10分数量相同，则比较9分的数量，以此类推，用例中不会出现多个选手得分完全相同的情况)。

输入描述:
第一行为半角逗号分割的两个正整数，第一个数字表示M（3<=M<=10）个评委，第二个数字表示N（3<=N<=100）个选手。
第2到M+1行是半角逗号分割的整数序列，表示评委为每个选手的打分，0号下标数字表示1号选手分数，1号下标数字表示2号选手分数，依次类推。
输出描述:
选手前3名的编号。
注：若输入为异常，输出-1，如M、N、打分不在范围内。

示例1：
输入
4,5
10,6,9,7,6
9,10,6,7,5
8,10,6,5,10
9,10,8,4,9
输出
2,1,5
说明
第一行代表有4个评委，5个选手参加比赛
矩阵代表是4*5，每个数字是选手的编号，每一行代表一个评委对选手的打分排序，
2号选手得分36分排第1，1号选手36分排第2，5号选手30分(2号10分值有3个，1号10分值只有1个，所以2号排第一)
示例2：
输入
2,5
7,3,5,4,2
8,5,4,4,3
输出
-1
说明
只有2个评委，要求最少为3个评委
示例3：
输入
4,2
8,5
5,6
10,4
8,9
输出
-1
说明
只有2名选手参加，要求最少为3名
示例4：
输入
4,5
11,6,9,7,8
9,10,6,7,8
8,10,6,9,7
9,10,8,6,7
输出
-1
说明
第一个评委给第一个选手打分11，无效分数

答案：
解法一（python）：
import sys

input = """
    4,5
10,6,9,7,6
9,10,6,7,5
8,10,6,5,10
9,10,8,4,9"""

if __name__ == "__main__":
    def slution():
        # 读取第一行的n
        try:
            p, x = sys.stdin.readline().strip().split(",")
            p = int(p)
            x = int(x)
        except:
            print(-1)
            return
        else:
            if (p >= 3 and p <= 10) and (x >= 3 and x <= 100):
                dp = [[0 for i in range(p)] for i in range(x)]
                for i in range(p):
                    try:
                        # 每一行的数据
                        line = sys.stdin.readline().strip().split(",")
                    except:
                        print(-1)
                        return
                    else:
                        for index, num in enumerate(line):
                            try:
                                num = int(num)
                                if num >= 1 and num <= 10:
                                    dp[index][i] = num
                                else:
                                    print(-1)
                                    return
                            except:
                                print(-1)
                                return
                res = []
                for index, i in enumerate(dp):
                    i.sort()
                    i.reverse()
                    res.append((sum(i), i, index+1))
                res.sort(key=lambda x: (x[0], x[1]))
                res.reverse()
                print(f"{res[0][2]},{res[1][2]},{res[2][2]}")
            else:
                print(-1)

    slution()


9、查找接口成功率最优时间段
服务之间交换的接口成功率作为服务调用关键质量特性，某个时间段内的接口失败率使用一个数组表示，数组中每个元素都是单位时间内失败率数值，数组中的数值为0~100的整数，给定一个数值(minAverageLost)表示某个时间段内平均失败率容忍值，即平均失败率小于等于minAverageLost，找出数组中最长时间段，如果未找到则直接返回NULL。

输入描述:
输入有两行内容，第一行为{minAverageLost}，第二行为{数组}，数组元素通过空格(" ")分隔，minAverageLost及数组中元素取值范围为0~100的整数，数组元素的个数不会超过100个。
输出描述:
找出平均值小于等于minAverageLost的最长时间段，输出数组下标对，格式{beginIndex}-{endIndx}(下标从0开始)，如果同时存在多个最长时间段，则输出多个下标对且下标对之间使用空格(" ")拼接，多个下标对按下标从小到大排序。

示例1：
输入
1
0 1 2 3 4
输出
0-2
说明
A、输入解释：minAverageLost=1，数组[0, 1, 2, 3, 4]
B、前3个元素的平均值为1，因此数组第一个至第三个数组下标，即0-2
示例2：
输入
2
0 0 100 2 2 99 0 2
输出
0-1 3-4 6-7
说明
A、输入解释：minAverageLost=2，数组[0, 0, 100, 2, 2, 99, 0, 2]
B、通过计算小于等于2的最长时间段为：数组下标为0-1即[0, 0]，数组下标为3-4即[2, 2]，数组下标为6-7即[0, 2]，这三个部分都满足平均值小于等2的要求，因此输出0-1 3-4 6-7

答案：
解法一：
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    private static List<String> sResultList = new ArrayList<>();
    private static int sCurrentLength = 0;
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNextLine()) {
            int minAvg = Integer.parseInt(scanner.nextLine().trim());
            String[] strings = scanner.nextLine().trim().split(" ");
            List<Integer> list = new ArrayList<Integer>();
            for (int i = 0; i < strings.length; i++) {
                list.add(Integer.parseInt(strings[i]));
            }
            getPeriod(minAvg, list);
            if (!sResultList.isEmpty()) {
                for (int i = 0; i < sResultList.size(); i++) {
                    System.out.print(sResultList.get(i));
                    System.out.print(" ");
                }
            }
        }
    }

    private static void getPeriod(int minAvg, List<Integer> list) {
        sResultList.clear();
        sCurrentLength = 0;
        for (int start = 0; start < list.size() - 1; start++) {
            for (int end  = start + 1; end < list.size(); end++) {
                int sum = getSum(list, start, end);
                String result = "";
                int length = end - start + 1;
                if (sum == 0 && minAvg >= 0) {
                    result = start + "-" + end;
                } else {
                    if (sum <= minAvg * length) {
                        result = start + "-" + end;
                    }
                }
                if (result.contains("-")) {
                    if (length == sCurrentLength) {
                        sResultList.add(result);
                    }
                    if (length > sCurrentLength) {
                        sResultList.clear();
                        sResultList.add(result);
                        sCurrentLength = length;
                    }
                }
            }
        }
    }

    private static int getSum(List<Integer> list, int start, int end) {
        int sum = 0;
        for (int i = start; i <= end; i++) {
            sum += list.get(i);
        }
        return sum;
    }
}

10、查找众数及中位数
1.众数是指一组数据中出现次数量多的那个数，众数可以是多个
2.中位数是指把一组数据从小到大排列，最中间的那个数，如果这组数据的个数是奇数，那最中间那个就是中位数，如果这组数据的个数为偶数，那就把中间的两个数之和除以2，所得的结果就是中位数
3.查找整型数组中元素的众数并组成一个新的数组，求新数组的中位数

输入描述:
输入一个一维整型数组，数组大小取值范围 0<N<1000，数组中每个元素取值范围 0<E<1000
输出描述:
输出众数组成的新数组的中位数

示例1：
输入
10 11 21 19 21 17 21 16 21 18 15
输出
21
示例2：
输入
2 1 5 4 3 3 9 2 7 4 6 2 15 4 2 4
输出
3
示例3：
输入
5 1 5 3 5 2 5 5 7 6 7 3 7 11 7 55 7 9 98 9 17 9 15 9 9 1 39
输出
7

答案：
解法一：
import java.util.*;
public class Main {
    public static void main(String[] args) {
        // 输入
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        String[] s = input.split(" ");
        int[] nums = new int[s.length];
        for (int i = 0; i < nums.length; i++) {
            nums[i] = Integer.parseInt(s[i]);
        }
        scanner.close();
        // 获取众数数组和中位数
        Integer[] manyNums = getManyArr(nums);
        int medium = 0;
        int len = manyNums.length;
        if (len % 2 == 0) {
            medium = (manyNums[len / 2 - 1] + manyNums[len / 2]) / 2;
        } else {
            medium = manyNums[len / 2];
        }
        System.out.println(medium);
    }

    private static Integer[] getManyArr(int[] arr) {
        if (arr == null) {
            return new Integer[0];
        }
        // 将数组元素和出现的次数转换为key-value
        Map<Integer, Integer> countMap = new HashMap<>();
        for (int i = 0; i < arr.length; i++) {
            int current = arr[i];
            if (countMap.containsKey(current)) {
                Integer count = countMap.get(current);
                countMap.put(current, ++count);
            } else {
                countMap.put(current, 1);
            }
        }
        // 获取出现最多的次数
        int countMax = 0;
        for (int value : countMap.values()) {
            if (value > countMax) {
                countMax = value;
            }
        }
        // 获取众数，并排序
        List<Integer> list = new ArrayList<>();
        for (int key : countMap.keySet()) {
            if (countMap.get(key) == countMax) {
                list.add(key);
            }
        }
        list.sort(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o1 - o2;
            }
        });
        Integer[] newArr = new Integer[list.size()];
        return list.toArray(newArr);
    }
}

解法二：
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        HashMap<Integer, Integer> map = new HashMap<>();
        int max = 0;
        List<Integer> list =new ArrayList<>();
        while (in.hasNextInt()) {
            int num = in.nextInt();
            map.merge(num,1,(a,b)->a+b);
            if (map.get(num)>max){
                list.clear();
                list.add(num);
                max = map.get(num);
            }else if (map.get(num)==max){
                list.add(num);
            }
        }
        list.sort(Integer::compare);
        int n = list.size();
        if (n%2==0){
            System.out.print((list.get(n/2)+list.get(n/2-1))/2);
        }else{
            System.out.print(list.get(n/2));
        }
    }
}


11、磁盘容量排序
磁盘的容量单位常用的有M，G，T这三个等级，它们之间的换算关系为1T = 1024G，1G = 1024M，现在给定n块磁盘的容量，请对它们按从小到大的顺序进行稳定排序，例如给定5块盘的容量，1T，20M，3G，10G6T，3M12G9M排序后的结果为20M，3G，3M12G9M，1T，10G6T。注意单位可以重复出现，上述3M12G9M表示的容量即为3M+12G+9M，和12M12G相等。

输入描述:
输入第一行包含一个整数n(2 <= n <= 100)，表示磁盘的个数，接下的n行，每行一个字符串(长度大于2，小于30)，表示磁盘的容量，由一个或多个格式为mv的子串组成，其中m表示容量大小，v表示容量单位，例如20M，1T，30G，10G6T，3M12G9M。

磁盘容量m的范围为1到1024的正整数，容量单位v的范围只包含题目中提到的M，G，T三种，换算关系如题目描述。
输出描述:
输出n行，表示n块磁盘容量排序后的结果。

示例1：
输入
3
1G
2G
1024M
输出
1G
1024M
2G
说明
1G和1024M容量相等，稳定排序要求保留它们原来的相对位置，故1G在1024M之前
示例2：
输入
3
2G4M
3M2G
1T
输出
3M2G
2G4M
1T
说明
1T的容量大于2G4M，2G4M的容量大于3M2G

答案：
解法一：
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int getSize(string s) {
    int ans = 0;
    int curNum = 0;
    for (char c: s) {
        if (isdigit(c)) {
            curNum = curNum * 10 + (c - '0');
        } else {
            if (c == 'M') {
                ans += curNum;
            } else if (c == 'G') {
                ans += curNum * 1024;
            } else if (c == 'T') {
                ans += curNum * 1024 * 1024;
            }
            curNum = 0;
        }
    }
    return ans;
}

bool cmp(const string& s1, const string& s2) {
    return getSize(s1) < getSize(s2);
}

int main() {
    string s;
    int n;
    cin >> n;
    vector<string> size;
    while(n--) {
        cin >> s;
        size.push_back(s);
    }
    stable_sort(size.begin(), size.end(), cmp);
    for (string s: size) {
        cout << s << endl;
    }
    return 0;
}

12、单词接龙
单词接龙的规则是：可用于接龙的单词首字母必须要前一个单词的尾字母相同；当存在多个首字母相同的单词时，取长度最长的单词，如果长度也相等，则取字典序最小的单词；已经参与接龙的单词不能重复使用。
现给定一组全部由小写字母组成单词数组，并指定其中的一个单词作为起始单词，进行单词接龙，请输出最长的单词串，单词串是单词拼接而成，中间没有空格。

输入描述:
输入的第一行为一个非负整数，表示起始单词在数组中的索引K，0 <= K < N ；
输入的第二行为一个非负整数，表示单词的个数N；
接下来的N行，分别表示单词数组中的单词。
输出描述:
输出一个字符串，表示最终拼接的单词串。

示例1：
输入
0
6
word
dd
da
dc
dword
d
输出
worddwordda
说明
先确定起始单词word，再接以d开头的且长度最长的单词dword，剩余以d开头且长度最长的有dd、da、dc，则取字典序最小的da，所以最后输出worddwordda。
示例2：
输入
4
6
word
dd
da
dc
dword
d
输出
dwordda
说明
先确定起始单词dword，剩余以d开头且长度最长的有dd、da、dc，则取字典序最小的da，所以最后输出dwordda。
备注:
单词个数N的取值范围为[1, 20]；
单个单词的长度的取值范围为[1, 30]；

答案：
解法一（python3）：
while True:
    try:
        index = int(input())
        n = int(input())
        data = []
        for _ in range(n):
            data.append(input())
        res = data[index]
        data.remove(data[index])
        for i in range(n - 1):
            target = res[-1]
            aa1 = []
            aa2=[]
            for j in data:
                if j.startswith(target):
                    aa1.append(j)
                    aa2.append(len(j))
            if aa1:
                max_len = max(aa2)
                if aa2.count(max_len)==1:
                    res+=aa1[aa2.index(max_len)]
                    data.remove(aa1[aa2.index(max_len)])
                else:
                    aa3=list(filter(lambda x:len(x)==max_len,aa1))
                    aa3.sort()
                    res+=aa3[0]
                    data.remove(aa3[0])
            else:
                break
        print(res)
    except:
        break

12、第k个排列
给定参数n，从1到n会有n个整数：1,2,3,…,n，这n个数字共有 n! 种排列。
按大小顺序升序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

输入描述:
输入两行，第一行为n，第二行为k，给定 n 的范围是 [1,9]，给定 k 的范围是[1,n!]。
输出描述:
输出排在第k位置的数字。

示例1：
输入
3
3
输出
213
说明
3的排列有123 132 213...，那么第3位置的为213
示例2：
输入
2
2
输出
21
说明
2的排列有12 21，那么第2位置的为21

答案：
解法一：
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        List<Integer> list = new ArrayList<>();
        int[] arr = new int[n + 1];
        arr[0] = 1;
        for (int i = 1; i <= n; i++) {
            list.add(i);
            arr[i] = arr[i - 1] * i;
        }
        k--;
        StringBuffer stringBuffer = new StringBuffer();
        for (int i = n - 1; i >= 0; i--) {
            int index = k / arr[i];
            stringBuffer.append(list.remove(index));
            k -= index * arr[i];
        }
        System.out.println(stringBuffer.toString());
    }
}

13、斗地主之顺子
在斗地主扑克牌游戏中， 扑克牌由小到大的顺序为：3,4,5,6,7,8,9,10,J,Q,K,A,2，玩家可以出的扑克牌阵型有：单张、对子、顺子、飞机、炸弹等。
其中顺子的出牌规则为：由至少5张由小到大连续递增的扑克牌组成，且不能包含2。
例如：{3,4,5,6,7}、{3,4,5,6,7,8,9,10,J,Q,K,A}都是有效的顺子；而{J,Q,K,A,2}、 {2,3,4,5,6}、{3,4,5,6}、{3,4,5,6,8}等都不是顺子。
给定一个包含13张牌的数组，如果有满足出牌规则的顺子，请输出顺子。
如果存在多个顺子，请每行输出一个顺子，且需要按顺子的第一张牌的大小（必须从小到大）依次输出。
如果没有满足出牌规则的顺子，请输出No。

输入描述:
13张任意顺序的扑克牌，每张扑克牌数字用空格隔开，每张扑克牌的数字都是合法的，并且不包括大小王：
2 9 J 2 3 4 K A 7 9 A 5 6
不需要考虑输入为异常字符的情况
输出描述:
组成的顺子，每张扑克牌数字用空格隔开：
3 4 5 6 7

示例1：
输入
2 9 J 2 3 4 K A 7 9 A 5 6
输出
3 4 5 6 7
说明
13张牌中，可以组成的顺子只有1组：3 4 5 6 7
示例2：
输入
2 9 J 10 3 4 K A 7 Q A 5 6
输出
3 4 5 6 7
9 10 J Q K A
说明
13张牌中，可以组成2组顺子，从小到大分别为：3 4 5 6 7 和 9 10 J Q K A
示例3：
输入
2 9 9 9 3 4 K A 10 Q A 5 6
输出
No
说明
13张牌中，无法组成顺子

答案：
解法一：
import java.util.*;
import java.util.stream.Collectors;

public class Main {

       public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNext()) {
            String inputPoker = scanner.nextLine();
            String[] allPoker = inputPoker.split(" ");

            Queue<Integer> sortedInput = Arrays
                    .stream(allPoker)
                    .filter(poker -> !poker.equals("2"))
                    .map(poker -> {
                        switch (poker) {
                            case "J":
                                return 11;
                            case "Q":
                                return 12;
                            case "K":
                                return 13;
                            case "A":
                                return 14;
                            default:
                                return Integer.parseInt(poker);
                        }
                    })
                    .sorted().collect(Collectors.toCollection(LinkedList::new));


            List<SortedBean> allSortedList = new ArrayList<>();
            int resultCount = 0;
            int lastValue = 0;
            while (!sortedInput.isEmpty()) {
                Integer currentValue = sortedInput.remove();

                if (lastValue == 0) {
                    SortedBean sortedBean = new SortedBean();
                    sortedBean.currLastValue = currentValue;
                    ArrayList<Integer> allData = new ArrayList<>();
                    allData.add(currentValue);
                    sortedBean.allData = allData;
                    allSortedList.add(sortedBean);
                } else {
                    if (currentValue - lastValue == 0) {
                        boolean isAdded = false;
                        for (SortedBean sortedBean : allSortedList) {
                            if (currentValue - sortedBean.currLastValue == 1) {
                                sortedBean.currLastValue = currentValue;
                                sortedBean.allData.add(currentValue);
                                isAdded = true;
                                break;
                            }
                        }

                        if (!isAdded) {
                            SortedBean sortedBean = new SortedBean();
                            sortedBean.currLastValue = currentValue;
                            ArrayList<Integer> allData = new ArrayList<>();
                            allData.add(currentValue);
                            sortedBean.allData = allData;
                            allSortedList.add(sortedBean);
                        }
                    } else if (currentValue - lastValue == 1) {
                        for (SortedBean sortedBean : allSortedList) {
                            if (sortedBean.currLastValue == lastValue) {
                                sortedBean.currLastValue = currentValue;
                                sortedBean.allData.add(currentValue);
                                break;
                            }
                        }
                    } else {
                        SortedBean sortedBean = new SortedBean();
                        sortedBean.currLastValue = currentValue;
                        ArrayList<Integer> allData = new ArrayList<>();
                        allData.add(currentValue);
                        sortedBean.allData = allData;
                        allSortedList.add(sortedBean);
                    }
                }
                lastValue = currentValue;
            }

            allSortedList.sort(Comparator.comparingInt(o -> o.allData.size()));

            for (SortedBean sortedBean : allSortedList) {
                if (sortedBean.allData.size() >= 5) {
                    StringBuilder stringBuilder = new StringBuilder();
                    for (Integer integer : sortedBean.allData) {
                        stringBuilder.append(getValue(integer)).append(" ");
                    }
                    System.out.println(stringBuilder.substring(0, stringBuilder.length() - 1));
                    resultCount++;
                }
            }


            if (resultCount == 0) {
                System.out.println("No");
            }
        }
    }

    private static String getValue(int src) {
        switch (src) {
            case 11:
                return "J";
            case 12:
                return "Q";
            case 13:
                return "K";
            case 14:
                return "A";
            default:
                return src + "";
        }
    }

    private static class SortedBean {
        public int currLastValue;
        private List<Integer> allData;

        @Override
        public String toString() {
            return "SortedBean{" +
                    "currLastValue=" + currLastValue +
                    ", allData=" + allData +
                    '}';
        }
    }
}

14、非严格递增连续数字序列
输入一个字符串仅包含大小写字母和数字，求字符串中包含的最长的非严格递增连续数字序列的长度（比如12234属于非严格递增连续数字序列）。

输入描述:
输入一个字符串仅包含大小写字母和数字，输入的字符串最大不超过255个字符。
输出描述:
最长的非严格递增连续数字序列的长度

示例1：
输入
abc2234019A334bc
输出
4
说明
2234为最长的非严格递增连续数字序列，所以长度为4。

答案：
解法一：
// 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        while (in.hasNext()) {// 注意，如果输入是多个测试用例，请通过while循环处理多个测试用例
            String str = in.nextLine();
            if (str.length()==1&&str.charAt(0)>='0'&&str.charAt(0)<='9'){
                System.out.println(1);
                continue;
            }
            boolean flag = false;
            char[] c = str.toCharArray();
            int size = str.length();
            int max = 1;
            int length = 1;
            for (int i = 1; i < size ; i++) {
                if ((c[i - 1] >= '0' && c[i - 1] <= '9') || (c[i] >= '0' && c[i] <= '9')) {
                    flag = true;
                }
                if (c[i-1] <= c[i]&&c[i-1]>='0'&&c[i]<='9') {
                    length++;
                    if (length > max) {
                        max = length;
                    }
                    continue;
                } else {
                    length = 1;
                }

            }
            if (flag == true) {
                System.out.println(max);
            } else {
                System.out.println(0);
            }
        }
    }
}

14、分班
幼儿园两个班的小朋友在排队时混在了一起，每位小朋友都知道自己是否与前面一位小朋友是否同班，请你帮忙把同班的小朋友找出来。
小朋友的编号为整数，与前一位小朋友同班用Y表示，不同班用N表示。

输入描述:
输入为空格分开的小朋友编号和是否同班标志。
比如：6/N 2/Y 3/N 4/Y，表示共4位小朋友，2和6同班，3和2不同班，4和3同班。
其中，小朋友总数不超过999，每个小朋友编号大于0，小于等于999。
不考虑输入格式错误问题。

输出描述:
输出为两行，每一行记录一个班小朋友的编号，编号用空格分开。且：
1、编号需要按照大小升序排列，分班记录中第一个编号小的排在第一行。
2、若只有一个班的小朋友，第二行为空行。
3、若输入不符合要求，则直接输出字符串ERROR。

示例1：
输入
1/N 2/Y 3/N 4/Y
输出
1 2
3 4
说明
2的同班标记为Y，因此和1同班。
3的同班标记为N，因此和1、2不同班。
4的同班标记为Y，因此和3同班。
所以1、2同班，3、4同班，输出为
1 2
3 4

答案：
解法一：
import java.util.*;
import java.util.ArrayList;
import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) {
        try{
            Scanner scan = new Scanner(System.in);
            String in = scan.nextLine();
            String[] a = in.split(" ");
            ArrayList<Integer> l1 = new ArrayList<Integer>(999);
            ArrayList<Integer> l2 = new ArrayList<Integer>(999);
            ArrayList<Integer> l0 = null;
            boolean same = true;
            for (int i = a.length - 1; i >= 0; i--) {
                Integer num = Integer.parseInt(a[i].substring(0,a[i].indexOf("/")));
                if(num<=0||num>999){
                    throw new Exception();
                }
                same = a[i].endsWith("Y");
                if (i == a.length - 1) {
                    l0 = l1;
                }
                l0.add(num);
                if(!same){
                    l0 = l0==l1?l2:l1;
                }
            }
            Collections.sort(l1);
            Collections.sort(l2);
            if(new HashSet(l1).size()<l1.size()||new HashSet(l2).size()<l2.size()){
                throw new Exception();
            }
            if(l2.size()!=0 && l1.get(0)>l2.get(0)){
                System.out.println(l2.stream().map(String::valueOf).collect(Collectors.joining(" ")));
                System.out.println(l1.stream().map(String::valueOf).collect(Collectors.joining(" ")));
            }else{
                System.out.println(l1.stream().map(String::valueOf).collect(Collectors.joining(" ")));
                System.out.println(l2.stream().map(String::valueOf).collect(Collectors.joining(" ")));
            }
        }catch(Exception e){
            System.out.println("ERROR");
        }
    }

}


15、分糖果
小明从糖果盒中随意抓一把糖果，每次小明会取出一半的糖果分给同学们。
当糖果不能平均分配时，小明可以选择从糖果盒中（假设盒中糖果足够）取出一个糖果或放回一个糖果。
小明最少需要多少次（取出、放回和平均分配均记一次），能将手中糖果分至只剩一颗

输入描述:
抓取的糖果数（<10000000000）：
15
输出描述:
最少分至一颗糖果的次数：
5

示例1：
输入
15
输出
5
备注:
解释：(1)15+1=16;(2)16/2=8;(3)8/2=4;(4)4/2=2;(5)2/2=1;

答案：
解法一:
import java.io.InputStream;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        long sum = scanner.nextLong();
        System.out.println(count(sum, 0));
    }

    private static int count(long sum, int count){
        if(sum <= 1){
            return count;
        }
        if(sum%2==0){
            return count(sum/2, count + 1);
        }
        return Math.min(count(sum + 1, count + 1), count(sum - 1,count + 1));
    }
}

15、高矮个子排队
现在有一队小朋友，他们高矮不同，我们以正整数数组表示这一队小朋友的身高，如数组{5,3,1,2,3}。
我们现在希望小朋友排队，以“高”“矮”“高”“矮”顺序排列，每一个“高”位置的小朋友要比相邻的位置高或者相等；每一个“矮”位置的小朋友要比相邻的位置矮或者相等；
要求小朋友们移动的距离和最小，第一个从“高”位开始排，输出最小移动距离即可。
例如，在示范小队{5,3,1,2,3}中，{5, 1, 3, 2, 3}是排序结果。{5, 2, 3, 1, 3} 虽然也满足“高”“矮”“高”“矮”顺序排列，但小朋友们的移动距离大，所以不是最优结果。
移动距离的定义如下所示：
第二位小朋友移到第三位小朋友后面，移动距离为1，若移动到第四位小朋友后面，移动距离为2；

输入描述:
排序前的小朋友，以英文空格的正整数：
4 3 5 7 8
注：小朋友<100个
输出描述:
排序后的小朋友，以英文空格分割的正整数：
4 3 7 5 8

示例1：
输入
4 1 3 5 2
输出
4 1 5 2 3
示例2：
输入
1 1 1 1 1
输出
1 1 1 1 1
说明
相邻位置可以相等
示例3：
输入
xxx
输出
[ ]
说明：
出现非法参数情况， 返回空数组
备注:
4（高）3（矮）7（高）5（矮）8（高）， 输出结果为最小移动距离，只有5和7交换了位置，移动距离都是1。

答案：
解法一：
import java.util.Scanner;
import java.util.LinkedList;
public class Main {
    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
        LinkedList<Integer> list = new LinkedList<Integer>();
        try {
            while (sc.hasNext()) {
                list.add(Integer.valueOf(sc.next()));
            }
        } catch (Exception e) {
            System.out.println("[]");
            return;
        }

        for (int i = 0; i < list.size() - 1; i++) {
            if (i % 2 == 0 && Integer.valueOf(list.get(i)) < Integer.valueOf(list.get(i + 1))) {
                int tmp = list.get(i);
                list.set(i, list.get(i + 1));
                list.set(i + 1, tmp);
            } else if (i % 2 == 1 && Integer.valueOf(list.get(i)) > Integer.valueOf(list.get(i + 1))) {
                int tmp = list.get(i);
                list.set(i, list.get(i + 1));
                list.set(i + 1, tmp);
            }
            //System.out.print(str[i]);
        }
        for (int i = 0; i < list.size(); i++) {
            if (i != list.size() - 1) {
                System.out.print(list.get(i) + " ");
            } else {
                System.out.println(list.get(i));
            }
        }
    }
}

16、工号不够用了怎么办？
3020年，空间通信集团的员工人数突破20亿人，即将遇到现有工号不够用的窘境。
现在，请你负责调研新工号系统。继承历史传统，新的工号系统由小写英文字母（a-z）和数字（0-9）两部分构成。新工号由一段英文字母开头，之后跟随一段数字，比如"aaahw0001","a12345","abcd1","a00"。注意新工号不能全为字母或者数字,允许数字部分有前导0或者全为0。
但是过长的工号会增加同事们的记忆成本，现在给出新工号至少需要分配的人数X和新工号中字母的长度Y，求新工号中数字的最短长度Z。

输入描述:
一行两个非负整数 X Y，用数字用单个空格分隔。
0< X <=2^50 - 1
0< Y <=5

输出描述:
输出新工号中数字的最短长度Z

示例1
输入
260 1
输出
1
示例2
输入
26 1
输出
1
说明
数字长度不能为0
示例3
输入
2600 1
输出
2

答案：
解法一：
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long x = sc.nextLong();
        int y = sc.nextInt();
        int z = 1;
        int f = (int) Math.pow(26, y);
        while (f * Math.pow(10, z) < x) {
            z++;
        }
        System.out.println(z);
    }
}

17、勾股数元组
如果3个正整数(a,b,c)满足a2 + b2 = c2的关系，则称(a,b,c)为勾股数（著名的勾三股四弦五），为了探索勾股数的规律，我们定义如果勾股数(a,b,c)之间两两互质（即a与b，a与c，b与c之间均互质，没有公约数），则其为勾股数元祖（例如(3,4,5)是勾股数元祖，(6,8,10)则不是勾股数元祖）。请求出给定范围[N,M]内，所有的勾股数元祖。

输入描述:
起始范围N，1 <= N <= 10000
结束范围M，N < M <= 10000
输出描述:
1.  a,b,c请保证a < b < c,输出格式：a b c；
2.  多组勾股数元祖请按照a升序，b升序，最后c升序的方式排序输出；
3.  给定范围中如果找不到勾股数元祖时，输出”NA”。

示例1：
输入
1
20
输出
3 4 5
5 12 13
8 15 17
说明
[1, 20]范围内勾股数有：(3 4 5)，(5 12 13)，(6 8 10)，(8 15 17)，(9 12 15)，(12 16 20)；其中，满足(a,b,c)之间两两互质的勾股数元祖有：(3 4 5)，(5 12 13)，(8 15 17)；按输出描述中顺序要求输出结果。
示例2：
输入
5
10
输出
NA
说明
[5, 10]范围内勾股数有：(6 8 10)；其中，没有满足(a,b,c)之间两两互质的勾股数元祖； 给定范围中找不到勾股数元祖，输出”NA”。

答案：
解法一：
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static List solution(int N, int M){
        List list = new ArrayList();
        for(int i = N; i <= M - 2; i++){
            for(int j = i + 1; j <= M - 1; j++){
                double k = Math.sqrt(i * i + j * j);
                long kk = (long)k;
                if(k - kk == 0 && k <= M && help(i, j) && help(i, (int)(k)) && help(j, (int)(k))){
                    list.add(new int[]{i, j, (int)k});
                }else if(k > M){
                    break;
                }
            }
        }
        return list;
    }

    public static boolean help(int l, int n){
        if(l < n){
            int temp = l;
            l = n;
            n = temp;
        }
        int p;
        while((p = l % n) != 0){
            l = n;
            n = p;
        }
        return n == 1;
    }

    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int M = scanner.nextInt();

        List<int[]> result = solution(N, M);
        if(result.size() > 0){
            for(int[] res : result){
                System.out.println(res[0] + " " + res[1] + " " + res[2]);
            }
        }else{
            System.out.println("NA");
        }
    }
}

18、喊7的次数重排
喊7是一个传统的聚会游戏，N个人围成一圈，按顺时针从1到N编号。编号为1的人从1开始喊数，下一个人喊的数字为上一个人的数字加1，但是当将要喊出来的数字是7的倍数或者数字本身含有7的话，不能把这个数字直接喊出来，而是要喊"过"。假定玩这个游戏的N个人都没有失误地在正确的时机喊了"过"，当喊到数字K时，可以统计每个人喊"过"的次数。

现给定一个长度为N的数组，存储了打乱顺序的每个人喊"过"的次数，请把它还原成正确的顺序，即数组的第i个元素存储编号i的人喊"过"的次数。

输入描述:
输入为一行，为空格分隔的喊"过"的次数，注意K并不提供，K不超过200，而数字的个数即为N。
输出描述:
输出为一行，为顺序正确的喊"过"的次数，也由空格分隔。

示例1：
输入
0 1 0
输出
1 0 0
说明
一共只有一次喊"过"，那只会发生在需要喊7时，按顺序，编号为1的人会遇到7，故输出1 0 0。注意，结束时的K不一定是7，也可以是8、9等，喊过的次数都是1 0 0。
示例2：
输入
0 0 0 2 1
输出
0 2 0 1 0
说明
一共有三次喊"过"，发生在7 14 17，按顺序，编号为2的人会遇到7 17，编号为4的人会遇到14，故输出0 2 0 1 0。

答案：
解法一：
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String s = reader.readLine();
        String[] s1 = s.split(" ");
        int count = 0;
        for (int i = 0; i < s1.length; i++) {
            count += Integer.parseInt(s1[i]);
        }
        int num = 6;
        for (int j = 0; j < count; ) {
            num++;
            if(num % 7 == 0 || (num+"").contains("7")){
                j ++;
            }
        }
        int[] arr = new int[s1.length];
        for (int i = 1; i <= num; i++) {
            if(i % 7 == 0 || (i+"").contains("7")){
                arr[i % s1.length]++;
            }
        }
        for (int i = 1; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.print(arr[0]);
    }
}

19、猴子爬山
一天一只顽猴想去从山脚爬到山顶，途中经过一个有个N个台阶的阶梯，但是这猴子有一个习惯： 每一次只能跳1步或跳3步，试问猴子通过这个阶梯有多少种不同的跳跃方式？

输入描述:
输入只有一个整数N（0<N<=50）此阶梯有多少个阶梯
输出描述:
输出有多少种跳跃方式（解决方案数）

示例1：
输入
50
输出
122106097
示例2：
输入
3
输出
2

答案：
解法一：
import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        while(sc.hasNext()){
            int n = sc.nextInt();
            Main m = new Main();
            int sum = m.jump(n);
            System.out.print(sum);
        }
    }

    public int jump(int n){
        if(n==1||n==2){
            return 1;
        }else if(n==3){
            return 2;
        }else{
            return jump(n-3)+jump(n-1);
        }
    }
}

20、滑动窗口最大和
有一个N个整数的数组，和一个长度为M的窗口，窗口从数组内的第一个数开始滑动直到窗口不能滑动为止，每次窗口滑动产生一个窗口和（窗口内所有数的和），求窗口滑动产生的所有窗口和的最大值。

输入描述:
第一行输入一个正整数N，表示整数个数。(0<N<100000)

第二行输入N个整数，整数的取值范围为[-100,100]。

第三行输入一个正整数M，M代表窗口大小，M<=100000，且M<=N。
输出描述:
窗口滑动产生的所有窗口和的最大值。

示例1：
输入
6
10 20 30 15 23 12
3
输出
68
说明
窗口长度为3，窗口滑动产生的窗口和分别为10+20+30=60，20+30+15=65，30+15+23=68，15+23+12=50，所以窗口滑动产生的所有窗口和的最大值为68。

答案：
解法一：
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] array = new int[n];
        for(int i = 0; i < n; i++){
            array[i] = sc.nextInt();
        }
        int m = sc.nextInt();
        int sum=0;
        for(int i=0;i<m;i++){
            sum+=array[i];
        }
        int max = sum;
        if(n>m){
            for(int i=0;i<(n-m);i++){
                sum += (array[m+i]-array[i]);
                if(sum>max){
                    max=sum;
                }
            }
        }
        System.out.println(max);
    }
}

21、火星文计算
已知火星人使用的运算符为#、$，其与地球人的等价公式如下：
x#y = 2*x+3*y+4
x$y = 3*x+y+2
1、其中x、y是无符号整数
2、地球人公式按C语言规则计算
3、火星人公式中，$的优先级高于#，相同的运算符，按从左到右的顺序计算
现有一段火星人的字符串报文，请你来翻译并计算结果。

输入描述:
火星人字符串表达式（结尾不带回车换行）
输入的字符串说明：  字符串为仅由无符号整数和操作符（#、$）组成的计算表达式。例如：123#4$5#67$78。
1、用例保证字符串中，操作数与操作符之间没有任何分隔符。
2、用例保证操作数取值范围为32位无符号整数。
3、保证输入以及计算结果不会出现整型溢出。
4、保证输入的字符串为合法的求值报文，例如：123#4$5#67$78
5、保证不会出现非法的求值报文，例如类似这样字符串：
#4$5 //缺少操作数
4$5# //缺少操作数
4#$5 //缺少操作数
4 $5 //有空格
3+4-5*6/7 //有其它操作符
12345678987654321$54321 //32位整数计算溢出
输出描述:
根据输入的火星人字符串输出计算结果（结尾不带回车换行）

示例1
输入
7#6$5#12
输出
226
说明
示例：
7#6$5#12
=7#(3*6+5+2)#12
=7#25#12
=(2*7+3*25+4)#12
=93#12
=2*93+3*12+4
=226

答案：
解法一：
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // x#y = 2*x+3*y+4  x$y = 3*x+y+2  $优先级高于#
        while (sc.hasNextLine()) {
            String input = sc.nextLine();
            System.out.print(func(input));
        }
        sc.close();

    }

    private static int func (String input) {
        //优先算最后
        int index = input.lastIndexOf("#");
        if (index!= -1) {
            String left = input.substring(0, index);
            String right = input.substring(index +1);
            int res = 2 * func(left) + 3 * func(right) + 4;
            return res;
        }
        // 优先算第一
        index = input.lastIndexOf("$");
        if (index != -1) {
            String left = input.substring(0, index);
            String right = input.substring(index +1);
            int res = 3 * func(left) + func(right) + 2;
            return res;
        }
        return Integer.parseInt(input);

    }
}

22、计算面积
绘图机器的绘图笔初始位置在原点（0, 0），机器启动后其绘图笔按下面规则绘制直线：
1）尝试沿着横向坐标轴正向绘制直线，直到给定的终点值E。
2）期间可通过指令在纵坐标轴方向进行偏移，并同时绘制直线，偏移后按规则1 绘制直线；指令的格式为X offsetY，表示在横坐标X 沿纵坐标方向偏移，offsetY为正数表示正向偏移，为负数表示负向偏移。

给定了横坐标终点值E、以及若干条绘制指令，请计算绘制的直线和横坐标轴、以及 X=E 的直线组成图形的面积。

输入描述:
首行为两个整数 N E，表示有N条指令，机器运行的横坐标终点值E。
接下来N行，每行两个整数表示一条绘制指令X offsetY，用例保证横坐标X以递增排序方式出现，且不会出现相同横坐标X。
取值范围：0 < N <= 10000, 0 <= X <= E <=20000, -10000 <= offsetY <= 10000。
输出描述:
一个整数，表示计算得到的面积，用例保证，结果范围在0~4294967295内

示例1：
输入
4 10
1 1
2 1
3 1
4 -2
输出
12
示例2：
输入
2 4
0 1
2 -2
输出
4

答案：
解法一：
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] a1 = sc.nextLine().split(" ");
		int count = Integer.valueOf(a1[0]);
		int total = Integer.valueOf(a1[1]);
		long result = 0;
		int last_x = 0, last_y = 0;
		for (int i = 0; i < count; i++) {
			String[] a2 = sc.nextLine().split(" ");
			int x = Integer.valueOf(a2[0]);
			int y = Integer.valueOf(a2[1]);
			result += (x - last_x) * Math.abs(last_y);;
			last_x = x;
			last_y += y;
		}
		result += (total - last_x) * Math.abs(last_y);
		System.out.println(result);
	}
}

23、计算最大乘积
给定一个元素类型为小写字符串的数组，请计算两个没有相同字符的元素 长度乘积的最大值，如果没有符合条件的两个元素，返回0。

输入描述:
输入为一个半角逗号分隔的小写字符串的数组，2 <= 数组长度<=100，0 < 字符串长度<= 50。
输出描述:
两个没有相同字符的元素 长度乘积的最大值。

示例1
输入
iwdvpbn,hk,iuop,iikd,kadgpf
输出
14
说明
数组中有5个元素。
iwdvpbn与hk无相同的字符，满足条件，iwdvpbn的长度为7，hk的长度为2，乘积为14（7*2）。
iwdvpbn与iuop、iikd、kadgpf均有相同的字符，不满足条件。
iuop与iikd、kadgpf均有相同的字符，不满足条件。
iikd与kadgpf有相同的字符，不满足条件。
因此，输出为14。

答案：
解法一：
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int maxValue = -1;
        String a = in.nextLine();
        if(a == null) {
            System.out.println(0);
        }
        String[] array = a.split(",");
        if(array.length == 1){
            System.out.println(0);
        }
        for(int i = 0; i< array.length; i++) {
            for(int j = i+1; j< array.length; j++) {
                if(equals(array[i], array[j])){
                    int a1 = array[i].length();
                    int b = array[j].length();
                    maxValue = Math.max(maxValue, a1*b);
                }
            }
        }
        System.out.println(maxValue == -1? 0 : maxValue);

    }
    public static boolean equals(String a, String b) {
        for(int i = 0; i< a.length(); i++) {
            for(int j = 0; j< b.length(); j++) {
                if(a.charAt(i) == b.charAt(j)){
                    return false;
                }
            }
        }
        return true;
    }
}

24、检查是否存在满足条件的数字组合
给定一个正整数数组，检查数组中是否存在满足规则的数字组合

规则：
A = B + 2C

输入描述:
第一行输出数组的元素个数。

接下来一行输出所有数组元素，用空格隔开。
输出描述:
如果存在满足要求的数，在同一行里依次输出规则里A/B/C的取值，用空格隔开。

如果不存在，输出0。

示例1：
输入
4
2 7 3 0
输出
7 3 2
说明
7 = 3 + 2 * 2
示例2：
输入
3
1 1 1
输出
0
说明
找不到满足条件的组合
备注:
1. 数组长度在3-100之间。

2. 数组成员为0-65535，数组成员可以重复，但每个成员只能在结果算式中使用一次。如：数组成员为[0, 0, 1, 5]，0出现2次是允许的，但结果0 = 0 + 2 * 0是不允许的，因为算式中使用了3个0。
3. 用例保证每组数字里最多只有一组符合要求的解。

答案：
解法一：
import java.util.Scanner;
public class Main{
    public static void main(String args[]){
        Scanner s = new Scanner(System.in);
        while(s.hasNext()){
            int length = s.nextInt();
            int arr[] = new int [length];
            for(int i=0;i<length;i++){
                arr[i] = s.nextInt();
            }
            sort(arr,0,length-1);
            int i;
            boolean end = false;
            for(i=0;i<length-1;i++){
                for(int j=0;j<length-1;j++){
                    if(j==i)
                        continue;
                    int sum = arr[i]+arr[j]*2;
                    if(sum>arr[length-1])
                        break;
                    int max = i>j ? i : j;
                    for(int k=max+1;k<length;k++){
                        if(sum == arr[k]){
                            System.out.println(arr[k]+" "+arr[i]+" "+arr[j]);
                            end = true;
                            break;
                        }
                    }
                    if(end)
                        break;
                }
                if(end)
                    break;
            }
            if(i==length-1){
                System.out.println(0);
        }
        }
    }
    static void sort(int arr[], int left, int right){
        if(left>=right)
            return;
        int sign = arr[left];
        int l = left;
        int r = right;
        while(l<r){
            while(arr[r]>=sign && l<r)
                r--;
            arr[l] = arr[r];

            while(arr[l]<=sign && l<r)
                l++;
            arr[r] = arr[l];

        }
        arr[l] = sign;
        sort(arr,left,r);
        sort(arr,l+1,right);
    }
}

25、矩阵扩散
存在一个m*n的二维数组，其成员取值范围为0或1。其中值为1的成员具备扩散性，每经过1S，将上下左右值为0的成员同化为1。二维数组的成员初始值都为0，将第[i,j]和[k,l]两个个位置上元素修改成1后，求矩阵的所有元素变为1需要多长时间。

输入描述:
输出数据中的前2个数字表示这是一个m*n的矩阵，m和n不会超过1024大小；中间两个数字表示一个初始扩散点位置为i,j；最后2个数字表示另一个扩散点位置为k,l。

输出描述:
输出矩阵的所有元素变为1所需要秒数。

示例1：
输入
4,4,0,0,3,3
输出
3
说明
输出数据中的前2个数字表示这是一个4*4的矩阵；中间两个数字表示一个初始扩散点位置为0,0；最后2个数字表示另一个扩散点位置为3,3。
给出的样例是一个很简单模型，初始点在对角线上，达到中间的位置分别为3次迭代，即3秒。所以输出为3。

26、矩阵最大值
给定一个仅包含0和1的N*N二维矩阵，请计算二维矩阵的最大值，计算规则如下：
1、 每行元素按下标顺序组成一个二进制数（下标越大越排在低位），二进制数的值就是该行的值。矩阵各行值之和为矩阵的值。
2、允许通过向左或向右整体循环移动每行元素来改变各元素在行中的位置。
      比如： [1,0,1,1,1]向右整体循环移动2位变为[1,1,1,0,1]，二进制数为11101，值为29。
                  [1,0,1,1,1]向左整体循环移动2位变为[1,1,1,1,0]，二进制数为11110，值为30。

输入描述:
1、输入的第一行为正整数，记录了N的大小，0 < N <= 20。
2、输入的第2到N+1行为二维矩阵信息，行内元素边角逗号分隔。
输出描述:
矩阵的最大值。

示例1：
输入
5
1,0,0,0,1
0,0,0,1,1
0,1,0,1,0
1,0,0,1,1
1,0,1,0,1
输出
122
说明
第一行向右整体循环移动1位，得到本行的最大值[1,1,0,0,0]，二进制值为11000，十进制值为24。
第二行向右整体循环移动2位，得到本行的最大值[1,1,0,0,0]，二进制值为11000，十进制值为24。
第三行向左整体循环移动1位，得到本行的最大值[1,0,1,0,0]，二进制值为10100，十进制值为20。
第四行向右整体循环移动2位，得到本行的最大值[1,1,1,0,0]，二进制值为11100，十进制值为28。
第五行向右整体循环移动1位，得到本行的最大值[1,1,0,1,0]，二进制值为11010，十进制值为26。
因此，矩阵的最大值为122。

答案：
解法一：
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int count = sc.nextInt();
        sc.nextLine();
        String[] m = new String[count];
        int result = 0;
        for (int i = 0; i < count; i++) {
            m[i] = sc.nextLine().replaceAll(",", "");
            int max = 0;
            String v = m[i];
            for (int j = 0; j < v.length(); j++) {
                if (max < Integer.parseInt(v, 2)) {
                    max = Integer.parseInt(v, 2);
                }
                v = v.substring(1, v.length()) + v.substring(0, 1);
            }
            result += max;
        }
        System.out.println(result);
    }

}

27、考勤信息
公司用一个字符串来表示员工的出勤信息：
absent：缺勤
late：迟到
leaveearly：早退
present：正常上班
现需根据员工出勤信息，判断本次是否能获得出勤奖，能获得出勤奖的条件如下：
缺勤不超过一次；没有连续的迟到/早退；任意连续7次考勤，缺勤/迟到/早退不超过3次

输入描述:
用户的考勤数据字符串，记录条数 >= 1；输入字符串长度<10000；不存在非法输入
如：
2
present
present absent present present leaveearly present absent
输出描述:
根据考勤数据字符串，如果能得到考勤奖，输出"true"；否则输出"false"，对于输入示例的结果应为：
true false

示例1：
输入
2
present
present present
输出
true true
示例2：
输入
2
present
present absent present present leaveearly present absent
输出
true false

答案：
解法一：
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int cnt;
        cnt = Integer.parseInt(sc.nextLine());
        String[] arr = new String[cnt];
        for (int i = 0; i < cnt; i++) {
            String s = sc.nextLine();
            arr[i] = s;
        }
        Main myTest = new Main();

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < cnt; i++) {
            if (arr[i] == null || arr[i].length() == 0)
                break;
            String[] split = arr[i].split(" ");
            int absentCnt = 0;

            int lastLastOrEarly = -1;
            boolean flag = false;
            for (int j = 0; j < split.length; j++) {

                if ("absent".equalsIgnoreCase(split[j])) {
                    absentCnt++;
                    if (absentCnt >= 2) {
                        sb.append("false ");
                        flag = true;
                        break;
                    }

                } else if ("late".equalsIgnoreCase(split[j]) || "leaveearly".equalsIgnoreCase(split[j])) {
                    if (lastLastOrEarly == -1) {
                        lastLastOrEarly = j;
                    } else {
                        if (j - lastLastOrEarly == 1) {
                            sb.append("false ");
                            flag = true;
                            break;
                        } else
                            lastLastOrEarly = j;
                    }
                }

                boolean b = myTest.judge7C(split, j);
                if (!b) {
                    sb.append("false ");
                    flag = true;
                    break;
                }
            }
            if (!flag)
                sb.append("true ");
        }
        System.out.println(sb.toString().trim());
    }

    private boolean judge7C(String[] split, int now) {
        int cnt = 0;
        if (now < 7) {
            for (int i = 0; i <= now; i++) {
                String s = split[i];
                if ("absent".equals(s) || "late".equals(s) || "leaveearly".equals(s)) {
                    cnt++;
                }
            }
        } else {
            for (int i = now - 6; i <= now; i++) {
                String s = split[i];
                if ("absent".equals(s) || "late".equals(s) || "leaveearly".equals(s)) {
                    cnt++;
                }
            }
        }
        return cnt <= 3;
    }
}

28、靠谱的车
程序员小明打了一辆出租车去上班。出于职业敏感，他注意到这辆出租车的计费表有点问题，总是偏大。

出租车司机解释说他不喜欢数字4，所以改装了计费表，任何数字位置遇到数字4就直接跳过，其余功能都正常。

比如：

1.     23再多一块钱就变为25；

2.     39再多一块钱变为50；

3.     399再多一块钱变为500；

小明识破了司机的伎俩，准备利用自己的学识打败司机的阴谋。

给出计费表的表面读数，返回实际产生的费用。

输入描述:
只有一行，数字N，表示里程表的读数。

(1<=N<=888888888)。

输出描述:
一个数字，表示实际产生的费用。以回车结束。

示例1：
输入
5
输出
4
说明
5表示计费表的表面读数。
4表示实际产生的费用其实只有4块钱。
示例2：
输入
17
输出
15
说明
17表示计费表的表面读数。
15表示实际产生的费用其实只有15块钱。
示例3：
输入
100
输出
81
说明
100表示计费表的表面读数。
81表示实际产生的费用其实只有81块钱。

答案：
解法一：
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int ans = n,temp = 0,k = 0,j = 1;
        while(n > 0){
            if (n % 10  > 4){
                temp  += (n % 10 - 1) * k + j ;
            }else {
                temp  += (n % 10) * k;
            }
            k = k * 9 + j;
            j *= 10;
            n /= 10;
        }
        System.out.println(ans - temp);
    }
}

29、快递运输
一辆运送快递的货车，运送的快递均放在大小不等的长方体快递盒中，为了能够装载更多的快递，同时不能让货车超载，需要计算最多能装多少个快递。
注：快递的体积不受限制，快递数最多1000个，货车载重最大50000。

输入描述:
第一行输入每个快递的重量，用英文逗号分隔，如：5,10,2,11
第二行输入货车的载重量，如：20
不需要考虑异常输入。
输出描述:
输出最多能装多少个快递，如：3

示例1：
输入
5,10,2,11
20
输出
3
说明
货车的载重量为20，最多只能放三个快递5、10、2，因此输出3

答案：
解法一：
import java.util.*;

public class Main {
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        String s = input.nextLine(); //快递重量 英文逗号隔开
        int w = input.nextInt(); //货车载重量
        String[] split = s.split(",");
        List list = new LinkedList<Integer>();
        for (int i=0;i<split.length;i++){
            list.add(Integer.valueOf(split[i]));
        }
        int minNum;
        int count = 0;
        while (true){
            minNum = 100000;
            //找出最小
            for (int i=0;i<list.size();i++){
                if (minNum>(Integer) list.get(i)){
                    minNum = (Integer) list.get(i);
                }
            }
            list.remove(Integer.valueOf(minNum));
            if (w-minNum<0){
                break;
            }
            w = w-minNum;
            count++;
        }
        System.out.println(count);

    }
}

30、连续字母长度
给定一个字符串，只包含大写字母，求在包含同一字母的子串中，长度第 k 长的子串的长度，相同字母只取最长的那个子串。

输入描述:
第一行有一个子串(1<长度<=100)，只包含大写字母。
第二行为 k的值
输出描述:
输出连续出现次数第k多的字母的次数。

示例1
输入
AAAAHHHBBCDHHHH
3
输出
2
说明
同一字母连续出现的最多的是A和H，四次；第二多的是H，3次，但是H已经存在4个连续的，故不考虑；下个最长子串是BB，所以最终答案应该输出2。
示例2
输入
AABAAA
2
输出
1
说明
同一字母连续出现的最多的是A，三次；第二多的还是A，两次，但A已经存在最大连续次数三次，故不考虑；下个最长子串是B，所以输出1
示例3
输入
ABC
4
输出
-1
说明
只含有3个包含同一字母的子串，小于k，输出-1
示例4
输入
ABC
2
输出
1
说明
三个子串长度均为1，所以此时k = 1，k=2，k=3这三种情况均输出1。特此说明，避免歧义。
备注:
若子串中只包含同一字母的子串数小于k，则输出-1

答案：
解法一：
import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        while(sc.hasNext()){
            String s = sc.next();
            int k=sc.nextInt();
            char[] cArray=s.toCharArray();
            Map<Character,Integer> map=new HashMap<>();
            Set<Character> set=new HashSet<>();
            map.put(cArray[0],1);
            for(int i=0;i<cArray.length;i++){
                int start=i;
                while(start+1<cArray.length && cArray[start]==cArray[start+1]){
                    start++;
                }
                char c=cArray[i];
                set.add(c);
                int time=map.getOrDefault(c,0);
                if(start-i+1>time){
                    map.put(c,start-i+1);
                }
                i=start;
            }
            List<Integer> list=new ArrayList<>();
            for(Character c:set){
                list.add(map.get(c));
            }
            list.sort((n1,n2)->n2-n1);
            if(k-1<list.size() && k>0){
                System.out.println(list.get(k-1));
            }else{
                System.out.println(-1);
            }
        }
    }
}

31、两数之和绝对值最小
给定一个从小到大的有序整数序列（存在正整数和负整数）数组 nums ，请你在该数组中找出两个数，其和的绝对值(|nums[x]+nums[y]|)为最小值，并返回这个绝对值。
每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

输入描述:
一个通过空格分割的有序整数序列字符串，最多1000个整数，且整数数值范围是 -65535~65535。
输出描述:
两数之和绝对值最小值

示例1
输入
-3 -1 5 7 11 15
输出
2
说明
因为 |nums[0] + nums[2]| = |-3 + 5| = 2 最小，所以返回 2

答案：
解法一：
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str;
        while ((str=br.readLine())!=null) {
            String[] nums=str.split(" ");
            int minNum=Integer.MAX_VALUE;
            for(int i=0;i<nums.length-1;i++){
                for(int  j=i+1;j<nums.length;j++){
                    int temp=Math.abs((Integer.valueOf(nums[i])+Integer.valueOf(nums[j])));

                    if(minNum>temp){
                        minNum=temp;
                    }
                }
            }
            System.out.println(minNum);
        }
    }
}


32、流水线
一个工厂有m条流水线，来并行完成n个独立的作业，该工厂设置了一个调度系统，在安排作业时，总是优先执行处理时间最短的作业。
现给定流水线个数m，需要完成的作业数n, 每个作业的处理时间分别为t1,t2…tn。请你编程计算处理完所有作业的耗时为多少？
当n>m时，首先处理时间短的m个作业进入流水线，其他的等待，当某个作业完成时，依次从剩余作业中取处理时间最短的进入处理。

输入描述:
第一行为2个整数（采用空格分隔），分别表示流水线个数m和作业数n；
第二行输入n个整数（采用空格分隔），表示每个作业的处理时长t1,t2…tn。
0< m,n<100，0<t1,t2…tn<100。
注：保证输入都是合法的。
输出描述:
输出处理完所有作业的总时长

示例1
输入
3 5
8 4 3 2 10
输出
13
说明
1、先安排时间为2、3、4的3个作业。
2、第一条流水线先完成作业，然后调度剩余时间最短的作业8。
3、第二条流水线完成作业，然后调度剩余时间最短的作业10。
4、总工耗时就是第二条流水线完成作业的时间13（3+10）。
drom
答案：
解法一：

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int m=sc.nextInt(); //流水线
        int n=sc.nextInt();//作业数目
        int time[]=new int[n];
        for(int i=0;i<n;i++){
            time[i]=sc.nextInt();
        }
        System.out.println(caculate(m,n,time));
    }

    public static int caculate(int m,int n,int time[]){
        Arrays.sort(time);
        int sum[]=new int[m]; //m条流水线，m个结果，取最大
        for(int i=0;i<n;i++){
           sum[i%m]+=time[i];
        }
        int res=0;
        for(int j=0;j<m;j++){
            res=Math.max(res,sum[j]);
        }
        return res;
    }
}

33、乱序整数序列两数之和绝对值最小
给定一个随机的整数（可能存在正整数和负整数）数组 nums ，请你在该数组中找出两个数，其和的绝对值(|nums[x]+nums[y]|)为最小值，并返回这个两个数（按从小到大返回）以及绝对值。
每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

输入描述:
一个通过空格分割的有序整数序列字符串，最多1000个整数，且整数数值范围是 [-65535, 65535]。
输出描述:
两数之和绝对值最小值

示例1
输入
-1 -3 7 5 11 15
输出
-3 5 2
说明
因为 |nums[0] + nums[2]| = |-3 + 5| = 2 最小，所以返回 -3 5 2

答案：
解法一：
import java.util.ArrayList;
import java.util.Comparator;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int total = 65535 * 2;// 记录和绝对值
		int[] index = new int[2];// 记录排序后数字数组下标
		Scanner sc = new Scanner(System.in);
		String dataList = sc.nextLine();
		// 将数字字符串转为数字数组，并排序
		String[] strArr = dataList.split(" ");
		ArrayList<Integer> dataNewList = new ArrayList<Integer>();
		for (int i = 0; i < strArr.length; i++) {
			dataNewList.add(Integer.valueOf(strArr[i]));
		}
		dataNewList.sort(Comparator.naturalOrder());// 升序排列

		// 冒泡法记录和绝对值最小值
		for (int i = 0; i < dataNewList.size(); i++) {
			for (int j = i + 1; j < dataNewList.size(); j++) {
				int temp = Math.abs(dataNewList.get(i) + dataNewList.get(j));
				if (temp <= total) {
					total = temp;
					index[0] = i;
					index[1] = j;
				}
			}
		}
		System.out.println(dataNewList.get(index[0]) + " "
				+ dataNewList.get(index[1]) + " " + total);
    }
}

34、内存资源分配
有一个简易内存池，内存按照大小粒度分类，每个粒度有若干个可用内存资源，用户会进行一系列内存申请，需要按需分配内存池中的资源，返回申请结果成功失败列表。分配规则如下：
1、分配的内存要大于等于内存申请量，存在满足需求的内存就必须分配，优先分配粒度小的，但内存不能拆分使用。
2、需要按申请顺序分配，先申请的先分配。
3、有可用内存分配则申请结果为true，没有可用内存分配则返回false。
注：不考虑内存释放。

输入描述:
输入为两行字符串：
第一行为内存池资源列表，包含内存粒度数据信息，粒度数据间用逗号分割，一个粒度信息内部用冒号分割，冒号前为内存粒度大小，冒号后为数量。资源列表不大于1024，每个粒度的数量不大于4096
第二行为申请列表，申请的内存大小间用逗号分隔。申请列表不大于100000
如：
64:2,128:1,32:4,1:128
50,36,64,128,127

输出描述:
输出为内存池分配结果。
如：
true,true,true,false,false

示例1
输入
64:2,128:1,32:4,1:128
50,36,64,128,127
输出
true,true,true,false,false
说明
内存池资源包含：64K共2个、128K共1个、32K共4个、1K共128个的内存资源；
针对50,36,64,128,127的内存申请序列，分配的内存依次是：64,64,128,NULL,NULL,第三次申请内存时已经将128分配出去，
因此输出结果是：true,true,true,false,false

答案：
解法一：
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String mem = scanner.nextLine();
        String app = scanner.nextLine();
        String[] mems = mem.split(",");
        String[] apps = app.split(",");
        if (mems.length > 1024 || apps.length >100000)
            return;
        Map<Integer,Integer> map = new LinkedHashMap<>();
        for (int i = 0;i<mems.length;i++){
            String[] tmp = mems[i].split(":");
            if (Integer.parseInt(tmp[1]) > 4096)
                return;
            map.put(Integer.parseInt(tmp[0]),Integer.parseInt(tmp[1]));
        }
        for (int i = 0;i<apps.length;i++){
            if (i > 0){
                System.out.print(",");
            }
            List<Integer> list = new ArrayList<>();
            for (Integer integer : map.keySet()){
                if (integer >= Integer.parseInt(apps[i])){
                    list.add(integer);
                }
            }
            if (list.size() > 0){
                Integer a = map.get(Collections.min(list));
                a = a - 1;
                if (a == 0){
                    map.remove(Collections.min(list));
                }else{
                    map.put(Collections.min(list),a);
                }
                System.out.print("true");
            }else{
                System.out.print("false");
            }
        }
    }
}


35、判断一组不等式是否满足约束并输出最大差
给定一组不等式，判断是否成立并输出不等式的最大差(输出浮点数的整数部分)，要求：1）不等式系数为double类型，是一个二维数组；2）不等式的变量为int类型，是一维数组；3）不等式的目标值为double类型，是一维数组；4）不等式约束为字符串数组，只能是：">",">=","<","<=","="，例如,不等式组：
a11*x1+a12*x2+a13*x3+a14*x4+a15*x5<=b1;
a21*x1+a22*x2+a23*x3+a24*x4+a25*x5<=b2;
a31*x1+a32*x2+a33*x3+a34*x4+a35*x5<=b3;

最大差=max{  (a11*x1+a12*x2+a13*x3+a14*x4+a15*x5-b1),   (a21*x1+a22*x2+a23*x3+a24*x4+a25*x5-b2),   (a31*x1+a32*x2+a33*x3+a34*x4+a35*x5-b3)  }，类型为整数(输出浮点数的整数部分)

输入描述:
1）不等式组系数(double类型)：
a11,a12,a13,a14,a15
a21,a22,a23,a24,a25
a31,a32,a33,a34,a35
2）不等式变量(int类型)：
x1,x2,x3,x4,x5
3）不等式目标值(double类型)：b1,b2,b3
4)不等式约束(字符串类型):<=,<=,<=

输入：a11,a12,a13,a14,a15;a21,a22,a23,a24,a25;a31,a32,a33,a34,a35;x1,x2,x3,x4,x5;b1,b2,b3;<=,<=,<=

输出描述:
true 或者 false, 最大差

示例1
输入
2.3,3,5.6,7,6;11,3,8.6,25,1;0.3,9,5.3,66,7.8;1,3,2,7,5;340,670,80.6;<=,<=,<=
输出
false 458
示例2
输入
2.36,3,6,7.1,6;1,30,8.6,2.5,21;0.3,69,5.3,6.6,7.8;1,13,2,17,5;340,67,300.6;<=,>=,<=
输出
false 758

答案：
解法一：
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        double [][] a = new double[3][5];
        int [] x = new int[5];
        double [] b = new double[3];
        String [] eqExpression = new String[3];
        int [] resultArrTemp = new int[3];
        int max = 0;
        Scanner scanner = new Scanner(System.in);
        boolean result = true;

        String lines = scanner.nextLine();
        String [] line = lines.split(";");

        //int i;
        for (int i = 0; i < 3; i++) {
            String [] temp1 = line[i].split(",");
            for (int j = 0; j < 5; j++) {
                a[i][j] = Double.valueOf(temp1[j]);
            }
        }
        String [] temp2 = line[3].split(",");
        for (int i = 0; i < 5; i++) {

            x[i] = Integer.valueOf(temp2[i]);
        }
        String [] temp3 = line[4].split(",");
        for (int i = 0; i < 3; i++) {

            b[i] = Double.valueOf(temp3[i]);
        }
        String [] temp4 = line[5].split(",");
        for (int i = 0; i < 3; i++) {
            eqExpression[i] = temp4[i];
        }

        for (int i = 0; i < 3; i++) {
            double temp=0.0;
            for (int j = 0; j < 5; j++) {
                temp = temp + a[i][j]*x[j];
            }
            if ("<=".equals(eqExpression[i])){
                if (temp<=b[i]){
                    result = result && true;
                    resultArrTemp[i] = (int) ((temp-b[i])/1);
                }else{
                    result = result && false;
                    resultArrTemp[i] = (int) ((temp-b[i])/1);
                }
            } else if ("<".equals(eqExpression[i])) {
                if (temp<b[i]){
                    result = result && true;
                    resultArrTemp[i] = (int) ((temp-b[i])/1);
                }else{
                    result = result && false;
                    resultArrTemp[i] = (int) ((temp-b[i])/1);
                }
            } else if ("=".equals(eqExpression[i])) {
                //String tempStr1 = String.valueOf(temp);
                //String tempStr2 = String.valueOf(b[i]);
                if (temp==b[i]){
                    result = result && true;
                    resultArrTemp[i] = (int) ((temp-b[i])/1);
                }else{
                    result = result && false;
                    resultArrTemp[i] = (int) ((temp-b[i])/1);
                }
            } else if (">".equals(eqExpression[i])) {
                if (temp>b[i]){
                    result = result && true;
                    resultArrTemp[i] = (int) ((temp-b[i])/1);
                }else{
                    result = result && false;
                    resultArrTemp[i] = (int) ((temp-b[i])/1);
                }
            } else if (">=".equals(eqExpression[i])) {
                if (temp>=b[i]){
                    result = result && true;
                    resultArrTemp[i] = (int) ((temp-b[i])/1);
                }else{
                    result = result && false;
                    resultArrTemp[i] = (int) ((temp-b[i])/1);
                }
            }
        }
        for (int i = 0; i < 3; i++) {
            if (i==0){
                max = resultArrTemp[i];
            }
            if (resultArrTemp[i]>=max){
                max = resultArrTemp[i];
            }
        }
        System.out.println(result+" "+max);
    }
}


36、判断字符串子序列
给定字符串 target和 source, 判断 target 是否为 source 的子序列。
你可以认为 target 和  source 中仅包含英文小写字母。字符串 source可能会很长（长度 ~= 500,000），而 target 是个短字符串（长度 <=100）。
字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"abc"是"aebycd"的一个子序列，而"ayb"不是）。
请找出最后一个子序列的起始位置。

输入描述:
第一行为target，短字符串（长度 <=100）
第二行为source，长字符串（长度 ~= 500,000）
输出描述:
最后一个子序列的起始位置， 即最后一个子序列首字母的下标

示例1
输入
abc
abcaybec
输出
3
说明
这里有两个abc的子序列满足，取下标较大的，故返回3
备注:
若在source中找不到target，则输出-1

答案：
解法一：
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        char[] tChars = scanner.nextLine().toCharArray();
        char[] sChars = scanner.nextLine().toCharArray();
        LinkedHashMap<Character, Integer> characterIntegerLinkedHashMap = new LinkedHashMap<Character, Integer>();
        int des=sChars.length;
        if (tChars.length>0&&sChars.length>0) {
            for (int j = tChars.length - 1; j >= 0; j--) {
                for (int i = sChars.length - 1; i >= 0; i--) {
                    if (tChars[j] == sChars[i] & des > i) {
                        des = i;
                        characterIntegerLinkedHashMap.put(tChars[j], i);
                        break;
                    }
                }
            }
            int ros = 0;
            for (int j = tChars.length - 1; j >= 0; j--) {
                if (!characterIntegerLinkedHashMap.containsKey(tChars[j])) {
                    ros = -1;
                    break;
                }
            }
            if (ros != -1) {
                System.out.println(characterIntegerLinkedHashMap.get(tChars[0]));
            } else {
                System.out.println(ros);
            }
        }else {
            System.out.println(-1);
        }
    }
}


37、拼接URL
给定一个URL前缀和URL后缀，通过","分割，需要将其连接为一个完整的URL，如果前缀结尾和后缀开头都没有“/”，需自动补上“/”连接符，如果前缀结尾和后缀开头都为“/”，需自动去重。
约束：不用考虑前后缀URL不合法情况。

输入描述:
URL前缀（一个长度小于100的字符串),URL后缀（一个长度小于100的字符串）。
输出描述:
拼接后的URL。

示例1
输入
/acm,/bb
输出
/acm/bb
示例2
输入
/abc/,/bcd
输出
/abc/bcd
示例3
输入
/acd,bef
输出
/acd/bef
示例4
输入
,
输出
/

答案：
解法一：
// 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        while (in.hasNextLine()) {// 注意，如果输入是多个测试用例，请通过while循环处理多个测试用例
            String inStr = in.nextLine();
            String out =  inStr.replaceFirst(",", "/");
            out = out.replace("//", "/");
            out = out.replace("//", "/");
            System.out.println(out);
        }
    }
}

38、求符合要求的结对方式
用一个数组A代表程序员的工作能力，公司想通过结对编程的方式提高员工的能力，假设结对后的能力为两个员工的能力之和，求一共有多少种结对方式使结对后能力为N。

输入描述:
5
1 2 2 2 3
4
第一行为员工的总人数，取值范围[1,1000]
第二行为数组A的元素，每个元素的取值范围[1,1000]
第三行为N的值，取值范围[1,1000]
输出描述:
4
满足结对后能力为N的结对方式总数

示例1
输入
5
1 2 2 2 3
4
输出
4
说明
满足要求的结对方式为：A[0]和A[4]，A[1]和A[2]，A[1]和A[3]，A[2]和A[3]

答案：
解法一：
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int total = sc.nextInt();
        int[] person = new int[total];
        for (int i = 0; i < total; i++) {
            person[i] = sc.nextInt();
        }

        int sum = sc.nextInt();
        int ans = 0;
        for (int i = 0; i < total; i++) {
            int persona = person[i];
            for (int j = i + 1; j < total; j++) {
                int personb = person[j];
                if (sum == persona + personb) {
                    ans++;
                }
            }
        }
        System.out.println(ans);
    }
}

39、求解连续数列
已知连续正整数数列{K}=K1,K2,K3...Ki的各个数相加之和为S，i=N (0<S<100000, 0<N<100000), 求此数列K。

输入描述:
输入包含两个参数，1）连续正整数数列和S，2）数列里数的个数N。
输出描述:
如果有解输出数列K，如果无解输出-1

示例1
输入
525 6
输出
85 86 87 88 89 90
示例2
输入
3 5
输出
-1

答案：
解法一：
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int sum = in.nextInt();
        int n = in.nextInt();
        // sum(x x+1 x+2 ... x+n-1) = sum
        // n*x + n*(n-1)/2 = sum
        // x= [sum - n*(n-1)/2 ]/n
        int temp = sum - n*(n-1)/2;
        if (temp <=0 || temp%n!=0){
            System.out.println(-1);
            return;
        }
        int begin = temp/n;
        for (int i = 0; i < n; i++) {
            System.out.print(begin+i);
            System.out.print(' ');
        }
    }
}

40、求字符串中所有整数的最小和
输入字符串s，输出s中包含所有整数的最小和
说明
1. 字符串s，只包含 a-z A-Z +- ；
2. 合法的整数包括
    1） 正整数 一个或者多个0-9组成，如 0 2 3 002 102
    2）负整数 负号 - 开头，数字部分由一个或者多个0-9组成，如 -0 -012 -23 -00023

输入描述:
包含数字的字符串
输出描述:
所有整数的最小和

示例1
输入
bb1234aa
输出
10
示例2
输入
bb12-34aa
输出
-31
说明
1+2+（-34） = 31

答案：
解法一：
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		// 计算 字符串中所有整数的最小和 ,字符串包括a-z+- ;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		char[] chars = input.toCharArray();
		char tmpChar;
		long sum = 0;
		// 负数的标记
		boolean flag = false;
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < chars.length; i++) {
			tmpChar = chars[i];
			// 判断字符 0-9 -
			if ('0' <= tmpChar && tmpChar <= '9') {
				if (flag) {
					// 减去最大的负数
					sb.append(tmpChar);
				} else {
					// 加上个位数的整数
					sum += Long.parseLong(tmpChar + "");
				}
			} else if ('-' == tmpChar) {
				if (flag) {
					if (!sb.toString().isEmpty()) {
						sum -= Long.parseLong(sb.toString());
						sb = new StringBuilder();
					}
				}
				flag = true;
			} else {
				flag = false;
				if (!sb.toString().isEmpty()) {
					sum -= Long.parseLong(sb.toString());
					sb = new StringBuilder();
				}
			}
		}
		if (flag) {
			if (!sb.toString().isEmpty()) {
				sum -= Long.parseLong(sb.toString());
			}
		}
		System.out.println(sum);
	}
}

41、求最多可以派出多少支团队
用数组代表每个人的能力，一个比赛活动要求参赛团队的最低能力值为N，每个团队可以由1人或2人组成，且1个人只能参加1个团队，请计算出最多可以派出多少支符合要求的团队？

输入描述:
5
3 1 5 7 9
8
第一行数组代表总人数，范围[1,500000]
第二行数组代表每个人的能力，每个元素的取值范围[1, 500000]，数组的大小范围[1,500000]
第三行数值为团队要求的最低能力值，范围[1, 500000]
输出描述:
3
最多可以派出的团队数量

示例1
输入
5
3 1 5 7 9
8
输出
3
说明
3,5组成一队，1,7组成一队，9自己一个队，故输出3

答案：
解法一：
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = in.nextInt();
        }
        int tar = in.nextInt();
        int res = 0;

        Arrays.sort(nums);
        int left = 0;
        int right = n-1;
        while (nums[right]>tar){
            right--;
            res++;
        }
        while (left<right){
            //两人团队
            if (nums[left]+nums[right]>=tar){
                res++;
                right--;
            }
            left++;
        }
        System.out.println(res);
    }
}

42、删除字符串中字符最少字符
删除字符串中出现次数最少的字符，如果有多个字符出现次数一样，则都删除。

输入描述:
输入abcdd
字符串中只包含小写英文字母。
输出描述:
dd

示例1
输入
abcdd
输出
dd
示例2
输入
aabbccdd
输出
empty
说明
如果字符串的字符都被删除，则范围empty

答案：
解法一：
import java.util.*;

public class Main {

    public static void main (String[] args) {
        Scanner scanner = new Scanner(System.in);
        String text = scanner.nextLine();
        char[] chars = text.toCharArray();
        Map<Character, Integer> char2times = new HashMap<>(10);
        for(int i = 0; i < chars.length; i++){
            if(char2times.containsKey(chars[i])){
                char2times.replace(chars[i], char2times.get(chars[i]) + 1);
            }else{
                char2times.put(chars[i], 1);
            }
        }
        int minTimes = Integer.MAX_VALUE;
        List<Character> minTimesChars = new ArrayList<>(5);
        for(Character character : char2times.keySet()){
            if(char2times.get(character) < minTimes){
                minTimes = char2times.get(character);
                minTimesChars.clear();
                minTimesChars.add(character);
            }else if(char2times.get(character) == minTimes){
                minTimesChars.add(character);
            }
        }
        for (Character minTimesChar : minTimesChars) {
            text = text.replaceAll(minTimesChar.toString(),"");
        }
        System.out.println("".equals(text) ? "empty" : text);
    }

}

43、数据分类
对一个数据a进行分类，分类方法为：此数据a（四个字节大小）的四个字节相加对一个给定的值b取模，如果得到的结果小于一个给定的值c，则数据a为有效类型，其类型为取模的值；如果得到的结果大于或者等于c，则数据a为无效类型。

比如一个数据a=0x01010101，b=3，按照分类方法计算（0x01+0x01+0x01+0x01）%3=1，所以如果c=2，则此a为有效类型，其类型为1，如果c=1，则此a为无效类型；

又比如一个数据a=0x01010103，b=3，按照分类方法计算（0x01+0x01+0x01+0x03）%3=0，所以如果c=2，则此a为有效类型，其类型为0，如果c=0，则此a为无效类型。

输入12个数据，第一个数据为c，第二个数据为b，剩余10个数据为需要分类的数据，请找到有效类型中包含数据最多的类型，并输出该类型含有多少个数据。

输入描述:
输入12个数据，用空格分隔，第一个数据为c，第二个数据为b，剩余10个数据为需要分类的数据。
输出描述:
输出最多数据的有效类型有多少个数据。

示例1
输入
3 4 256 257 258 259 260 261 262 263 264 265
输出
3
说明
10个数据4个字节相加后的结果分别为1 2 3 4 5 6 7 8 9 10，故对4取模的结果为1 2 3 0 1 2 3 0 1 2，c为3，所以0 1 2都是有效类型，类型为1和2的有3个数据，类型为0的只有2个数据，故输出3
示例2
输入
1 4 256 257 258 259 260 261 262 263 264 265
输出
2
说明
10个数据4个字节相加后的结果分别为1 2 3 4 5 6 7 8 9 10，故对4取模的结果为1 2 3 0 1 2 3 0 1 2，c为1，所以只有0是有效类型，类型为0的有2个数据，故输出2

答案：
解法一：
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNext()) {
            // 取数据
            int c = sc.nextInt();
            int b = sc.nextInt();
            final int size = 10;
            int[] num = new int[size];
            for (int i = 0; i < size; i++) {
                num[i] = sc.nextInt();
            }
            // type记录10个数各自的有效类型，无效记录-1
            int[] type = new int[size];
            // 计算有效类型
            for (int i = 0; i < size; i++) {
                type[i] = getValidType(num[i], b, c);
                // System.out.print(i + "=" + type[i] + ", ");
            }
            // 计算类型最多的数据个数
            int maxCount = 0;
            int count = 0;
            for (int i = 0; i < c; i++) {
                count = 0;
                for (int k = 0; k < size; k++) {
                    if (i == type[k]) {
                        count++;
                    }
                }
                if (count > maxCount) {
                    maxCount = count;
                }
            }
            // 输出结果
            System.out.println(maxCount);
        }
    }

    private static int getValidType(int num, int b, int c) {
        // int转换为4个字节相加
        int sum = 0;
        for (int i = 0; i < 4; i++) {
            sum += num % 256;
            num /= 256;
        }
        int mod = sum % b;
        return mod < c ? mod : -1;
    }
}

44、数列描述
有一个数列a[N] (N=60)，从a[0]开始，每一项都是一个数字。数列中a[n+1]都是a[n]的描述。其中a[0]=1。

规则如下：

a[0]:1

a[1]:11(含义：其前一项a[0]=1是1个1，即“11”。表示a[0]从左到右，连续出现了1次“1”）

a[2]:21(含义：其前一项a[1]=11，从左到右：是由两个1组成，即“21”。表示a[1]从左到右，连续出现了两次“1”)

a[3]:1211(含义：其前一项a[2]=21，从左到右：是由一个2和一个1组成，即“1211”。表示a[2]从左到右，连续出现了1次“2”，然后又连续出现了1次“1”)

a[4]:111221(含义：其前一项a[3]=1211，从左到右：是由一个1、一个2、两个1组成，即“111221”。表示a[3]从左到右，连续出现了1次“1”，连续出现了1次“2”，连续出现了两次“1”)

请输出这个数列的第n项结果（a[n]，0≤n≤59）。

输入描述:
数列的第n项(0≤n≤59)：
4
输出描述:
数列的内容：
111221

示例1
输入
4
输出
111221

答案：
解法一：
import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        int count=new Scanner(System.in).nextInt()+1;
        String[] raw = new String[count];
        raw[0]="1";
        for(int i=1;i<count;i++){
            StringBuilder builder=new StringBuilder();
            char[] lastStr=raw[i-1].toCharArray();
            char now=lastStr[0];
            int charCount=1;
            int index=1;
            while(index<lastStr.length){
                if(lastStr[index]==now) charCount++;
                else{
                    builder.append(charCount).append(now);
                    now = lastStr[index];
                    charCount=1;
                }
                index++;
            }
            builder.append(charCount).append(now);
            raw[i]=builder.toString();
        }
        System.out.println(raw[count-1]);
    }
}

45、数字涂色
疫情过后，希望小学终于又重新开学了，三年二班开学第一天的任务是将后面的黑板报重新制作。黑板上已经写上了N个正整数，同学们需要给这每个数分别上一种颜色。为了让黑板报既美观又有学习意义，老师要求同种颜色的所有数都可以被这种颜色中最小的那个数整除。现在请你帮帮小朋友们，算算最少需要多少种颜色才能给这N个数进行上色。

输入描述:
第一行有一个正整数N，其中1 \leq N \leq 1001≤N≤100。
第二行有N个int型数(保证输入数据在[1,100]范围中)，表示黑板上各个正整数的值。
输出描述:
输出只有一个整数，为最少需要的颜色种数。

示例1
输入
3
2 4 6
输出
1
说明
所有数都能被2整除
示例2
输入
4
2 3 4 9
输出
2
说明
2与4涂一种颜色，4能被2整除；3与9涂另一种颜色，9能被3整除。不能4个数涂同一个颜色，因为3与9不能被2整除。所以最少的颜色是两种。

答案:
解法一：
import com.sun.imageio.plugins.common.I18N;

import java.util.*;
import java.util.stream.Collectors;

public class Main {

    public static void main(String [] args){
        Scanner input = new Scanner(System.in);
        Map<Integer,List<Integer>> result = new HashMap<>();
        List<Integer> numList = new ArrayList<>();
        while(input.hasNext()){
            Integer N = input.nextInt();
            for(int i=0;i<N;i++){
                numList.add(input.nextInt());
            }
            numList = numList.stream().sorted().collect(Collectors.toList());
            for(int i =0;i<numList.size();i++){
                if(i==0){
                    List<Integer> singleList = new ArrayList<>();
                    singleList.add(numList.get(i));
                    result.put(numList.get(i),singleList);
                }else{
                    List<Map.Entry<Integer,List<Integer>>> mapList = result.entrySet().stream().collect(Collectors.toList());
                    for(int j=0;j<mapList.size();j++){
                        if(numList.get(i)%mapList.get(j).getKey()==0){
                            result.get(mapList.get(j).getValue().add(numList.get(i)));
                            break;
                        }else {
                            if(j==mapList.size()-1){
                                List<Integer> singleList = new ArrayList<>();
                                singleList.add(numList.get(i));
                                result.put(numList.get(i),singleList);
                            }
                        }

                    }
                }
            }
            System.out.println(result.size());
        }
    }
}

46、数组二叉树
二叉树也可以用数组来存储，给定一个数组，树的根节点的值存储在下标1，对于存储在下标N的节点，它的左子节点和右子节点分别存储在下标2*N和2*N+1，并且我们用值-1代表一个节点为空。

给定一个数组存储的二叉树，试求从根节点到最小的叶子节点的路径，路径由节点的值组成。

输入描述:
输入一行为数组的内容，数组的每个元素都是正整数，元素间用空格分隔。注意第一个元素即为根节点的值，即数组的第N个元素对应下标N，下标0在树的表示中没有使用，所以我们省略了。输入的树最多为7层。
输出描述:
输出从根节点到最小叶子节点的路径上，各个节点的值，由空格分隔，用例保证最小叶子节点只有一个。

示例1
输入
3 5 7 -1 -1 2 4
输出
3 7 2
说明
数组存储的二叉树如图，故到最小叶子节点的路径为3 7 2
示例2
输入
5 9 8 -1 -1 7 -1 -1 -1 -1 -1 6
输出
5 8 7 6
说明
数组存储的二叉树如图，故到最小叶子节点的路径为10 8 7 6，注意数组仅存储至最后一个非空节点，故不包含节点“7”右子节点的-1

答案：
解法一：
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        ArrayList<Integer> array = new ArrayList<>();

        while (in.hasNextInt()) {
            array.add(in.nextInt());
        }
        fun(array);

    }

    private static int dfs(List<Integer> nums, int index) {
        if (isLeaf(nums, index)) {
            return index;
        } else {
            int i1 = dfs(nums, 2 * index + 1);
            int i2 = dfs(nums, 2 * index + 2);
            if (i1 >= nums.size() || nums.get(i1) == -1) {
                return i2;
            } else if (i2 >= nums.size() || nums.get(i2) == -1) {
                return i1;
            } else {
                return nums.get(i1) < nums.get(i2) ? i1 : i2;
            }
        }
    }

    private static boolean isLeaf(List<Integer> nums, int index) {
        return (2 * index + 1 >= nums.size() || nums.get(2 * index + 1) == -1)
                && (2 * index + 2 >= nums.size() || nums.get(2 * index + 2) == -1);
    }

    private static void fun(List<Integer> nums) {
        int index = dfs(nums, 0);
        ArrayList<Integer> arr = new ArrayList<>();
        while (index > 0) {
            arr.add(nums.get(index));
            index = (index - 1) / 2;
        }
        arr.add(nums.get(0));

        Collections.reverse(arr);
        for (Integer integer : arr) {
            System.out.print(integer + " ");
        }
    }
}

47、数组拼接
现在有多组整数数组，需要将它们合并成一个新的数组。合并规则，从每个数组里按顺序取出固定长度的内容合并到新的数组中，取完的内容会删除掉，如果该行不足固定长度或者已经为空，则直接取出剩余部分的内容放到新的数组中，继续下一行。

输入描述:
第一行是每次读取的固定长度，0<长度<10
第二行是整数数组的数目，0<数目<1000
第3-n行是需要合并的数组，不同的数组用回车换行分隔，数组内部用逗号分隔，最大不超过100个元素。
输出描述:
输出一个新的数组，用逗号分隔。

示例1
输入
3
2
2,5,6,7,9,5,7
1,7,4,3,4
输出
2,5,6,1,7,4,7,9,5,3,4,7
说明
1、获得长度3和数组数目2。
2、先遍历第一行，获得2,5,6；
3、再遍历第二行，获得1,7,4；
4、再循环回到第一行，获得7,9,5；
5、再遍历第二行，获得3,4；
6、再回到第一行，获得7，按顺序拼接成最终结果。
示例2
输入
4
3
1,2,3,4,5,6
1,2,3
1,2,3,4
输出
1,2,3,4,1,2,3,1,2,3,4,5,6

答案：
解法一：
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextLine()) {
            int len = Integer.parseInt(sc.nextLine());
            int arrNum = Integer.parseInt(sc.nextLine());
            String[][] strArr = new String[arrNum][];
            int maxLen = 0;
            for (int i = 0; i < arrNum; i++){
                String str = sc.nextLine();
                if (str.length() > 0){
                    strArr[i] = str.split(",");
                    if (strArr[i].length > maxLen){
                        maxLen = strArr[i].length;
                    }
                }
            }
            int index = 0;
            StringBuilder sb = new StringBuilder();
            while (index < maxLen){
                for (int i = 0; i < arrNum; i++){
                    String[] arr = strArr[i];
                    if (arr == null){
                        continue;
                    }
                    for (int j = index; j < index + len; j++){
                        if (j < arr.length){
                            sb.append(arr[j]).append(",");
                        }
                    }
                }
                index += len;
            }
            int lastIndex = sb.lastIndexOf(",");
            if (lastIndex != -1){
                sb.deleteCharAt(lastIndex);
            }
            System.out.println(sb);
        }
    }
}

48、数组去重和排序
给定一个乱序的数组，删除所有的重复元素，使得每个元素只出现一次，并且按照出现的次数从高到低进行排序，相同出现次数按照第一次出现顺序进行先后排序。

输入描述:
一个数组
输出描述:
去重排序后的数组

示例1
输入
1,3,3,3,2,4,4,4,5
输出
3,4,1,2,5

备注:
数组大小不超过100
数组元素值大小不超过100

答案：
解法一：
import java.util.Scanner;
import java.util.LinkedHashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Set;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        String[] numbers = line.split(",");
        int[] ints = new int[numbers.length];
        for (int i = 0; i < ints.length; i++) {
            ints[i] = Integer.valueOf(numbers[i]);
        }
        LinkedHashMap<Integer, Integer> map = new LinkedHashMap<>();
        for (int i = 0; i < ints.length; i++) {
            if (map.isEmpty()) {
                map.put(ints[i], 1);
            } else {
                if (map.containsKey(ints[i])) {
                    int value = map.get(ints[i]);
                    value++;
                    map.put(ints[i], value);
                } else {
                    map.put(ints[i], 1);
                }
            }

        }
        Set<Map.Entry<Integer, Integer>> set = map.entrySet();
        LinkedList<Map.Entry<Integer, Integer>> list = new LinkedList<>(set);
        list.sort((o1, o2) -> o2.getValue() - o1.getValue());
        for (int i = 0; i < list.size(); i++) {
            Map.Entry<Integer, Integer> entry = list.get(i);
            if (i != list.size() - 1) {
                System.out.print(entry.getKey() + ",");
            } else {
                System.out.println(entry.getKey());
            }
        }
    }
}

49、数组组成的最小数字
给定一个整型数组，请从该数组中选择3个元素组成最小数字并输出（如果数组长度小于3，则选择数组中所有元素来组成最小数字）。

输入描述:
一行用半角逗号分割的字符串记录的整型数组，0 < 数组长度 <= 100，0 < 整数的取值范围 <= 10000。

输出描述:
由3个元素组成的最小数字，如果数组长度小于3，则选择数组中所有元素来组成最小数字。

示例1
输入
21,30,62,5,31
输出
21305
说明
数组长度超过3，需要选3个元素组成最小数字，21305由21,30,5三个元素组成的数字，为所有组合中最小的数字
示例2
输入
5,21
输出
215
说明
数组长度小于3， 选择所有元素来主城最小值，215为最小值。

答案：
解法一：
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        //获取输入存到数组中
        Scanner scanner = new Scanner(System.in);
        String inputString = scanner.nextLine();
        String[] numberArr = inputString.split(",");


        //计算
        if(numberArr.length<=0){
            return;
        }else if(numberArr.length ==1 ){ //只有一个数，直接输出
            System.out.println(numberArr[0]);
        }else if(numberArr.length ==2 ){ //有两个数，排列组合一下就行
            int s1 = Integer.parseInt(numberArr[0] + numberArr[1]);
            int s2 = Integer.parseInt(numberArr[1] + numberArr[0]);
            System.out.println(s1<s2?s1:s2);
        }else { //有3个数以上，先排序找出最小的三个数在进行组合
            Arrays.sort(numberArr, new Comparator<String>() {
                @Override
                public int compare(String o1, String o2) {
                    return Integer.parseInt(o1)-Integer.parseInt(o2);
                }
            });

            String[] min3Num = Arrays.copyOf(numberArr,3);

            Arrays.sort(min3Num);

            String res="";
            for (String s:min3Num){
                res += s;
            }
            System.out.println(res);
        }


    }
}

50、水仙花数
所谓水仙花数，是指一个n位的正整数，其各位数字的n次方和等于该数本身。例如153是水仙花数，153是一个3位数，并且153 = 1^3 + 5^3 + 3^3。

输入描述:
第一行输入一个整数n，表示一个n位的正整数。n在3到7之间，包含3和7。
第二行输入一个正整数m，表示需要返回第m个水仙花数。
输出描述:
返回长度是n的第m个水仙花数。个数从0开始编号。
若m大于水仙花数的个数，返回最后一个水仙花数和m的乘积。
若输入不合法，返回-1。

示例1
输入
3 0
输出
153
说明
153是第一个水仙花数
示例2
输入
9
1
输出
-1
说明
9超出范围

答案：
解法一：
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main{
      public static void main(String[] args) {
        //水仙数个数
        calcute1();
    }

       public static void calcute1(){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();//位数
        if (n >= 3 && n <= 7){
            int m = sc.nextInt();//第几个
            int temp = 1;
            for (int i = 0 ; i < n ; i ++){
                temp *= 10;
            }
            int min = temp / 10;
            int max = temp- 1;
            Map<Integer, Integer> data = new HashMap<>();
            int count = 0;
            int lastNum = 0;
            for (int i = min ; i <= max ; i ++){
                if (isRightNum(i, n)) {
                    data.put(count++, i);
                    if (i > lastNum){
                        lastNum = i;
                    }
                }
            }
            if (data.containsKey(m)){
                System.out.println(data.get(m));
            } else {
                System.out.println(lastNum * m);
            }
        } else {
            System.out.println(-1);
        }
    }

    public static boolean isRightNum(int num, int n){
        boolean result = false;
        String[] numStrs = String.valueOf(num).split("");
        int[] data = new int[numStrs.length];
        for (int i = 0 ; i < numStrs.length; i ++){
            data[i] = Integer.parseUnsignedInt(numStrs[i]);
        }
        int sum = 0;
        for (int i = 0 ; i < n ; i ++){
            sum += getCalcuteNum(data[i], n);
        }
        if (sum == num){
            result = true;
        }
        return result;
    }

    public static int getCalcuteNum(int a, int b){
        int result = 1;
        for (int i = 0; i < b ; i ++){
            result *=a;
        }
        return result;
    }
}

51、素数之积
RSA加密算法在网络安全世界中无处不在，它利用了极大整数因数分解的困难度，数据越大，安全系数越高，给定一个32位正整数，请对其进行因数分解，找出是哪两个素数的乘积。

输入描述:
一个正整数num
0 < num <= 2147483647
输出描述:
如果成功找到，以单个空格分割，从小到大输出两个素数，分解失败，请输出-1 -1

示例1
输入
15
输出
3 5
说明
因数分解后，找到两个素数3和5，使得3*5=15，按从小到大排列后，输出3 5

示例2
输入
27
输出
-1 -1
说明
通过因数分解，找不到任何素数，使得他们的乘积为27，输出-1 -1

答案：
解法一：
import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        long num = sc.nextLong();
        long limit = (long)Math.floor(Math.sqrt(num));
        String res = "";
        boolean flag = false;
        for(long i = 2;i<=limit;i++){
            if(num%i==0){
                if(isPrime(i)&&isPrime(num/i)){
                    flag = true;
                    if(i<num/i){
                        res = i+" "+num/i;
                    }
                    else{
                        res = num/i+" "+i;
                    }
                }
            }
        }
        if(flag==true){
            System.out.println(res);
        }
        else{
            System.out.println("-1 -1");
        }
    }

    public static boolean isPrime(long num){
        long limit = (long)Math.floor(Math.sqrt(num));
        for(long i = 2;i<=limit;i++){
            if(num%i==0) return false;
        }
        return true;
    }

}

52、太阳能板最大面积
给航天器一侧加装长方形或正方形的太阳能板（图中的红色斜线区域），需要先安装两个支柱（图中的黑色竖条），再在支柱的中间部分固定太阳能板。但航天器不同位置的支柱长度不同，太阳能板的安装面积受限于最短一侧的那根支柱长度。如图：
现提供一组整形数组的支柱高度数据，假设每根支柱间距离相等为1个单位长度，计算如何选择两根支柱可以使太阳能板的面积最大。

输入描述:
10,9,8,7,6,5,4,3,2,1
注：支柱至少有2根，最多10000根，能支持的高度范围1~10^9的整数。柱子的高度是无序的，例子中递减只是巧合。
输出描述:
可以支持的最大太阳能板面积：（10米高支柱和5米高支柱之间）
25

示例1
输入
10,9,8,7,6,5,4,3,2,1
输出
25
备注:
10米高支柱和5米高支柱之间宽度为5，高度取小的支柱高也是5，面积为25。任取其他两根支柱所能获得的面积都小于25。所以最大的太阳能板面积为25。

答案：
解法一：
import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] strs = sc.nextLine().split(",");
        int len = strs.length;
        long res = 0;
        for(int i = 0; i < len - 1; i++) {
            for(int j = i + 1; j < len; j++) {
                long a = Long.valueOf(strs[i]);
                long b = Long.valueOf(strs[j]);
                long c = j - i;
                if (a > b){
                    if (res < b * c)
                    res = b * c;
                }else{
                    if (res < a *c)
                    res = a * c;
                }
            }
        }
        System.out.print(res);
    }
}

53、停车场车辆统计
特定大小的停车场，数组cars[]表示，其中1表示有车，0表示没车。车辆大小不一，小车占一个车位（长度1），货车占两个车位（长度2），卡车占三个车位（长度3），统计停车场最少可以停多少辆车，返回具体的数目。

输入描述:
整型字符串数组cars[]，其中1表示有车，0表示没车，数组长度小于1000。
输出描述:
整型数字字符串，表示最少停车数目。

示例1
输入
1,0,1
输出
2
说明
1个小车占第1个车位
第二个车位空
1个小车占第3个车位
最少有两辆车
示例2
输入
1,1,0,0,1,1,1,0,1
输出
3
说明
1个货车占第1、2个车位
第3、4个车位空
1个卡车占第5、6、7个车位
第8个车位空
1个小车占第9个车位
最少3辆车

答案：
解法一：
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        while (scan.hasNext()) {
            String line = scan.next();
            if(line.split(",").length >= 1000){
                System.out.println(0);
                continue;
            }
            int result = 0;
            String[] split = line.replaceAll(",", "").split("0+");
            if(split != null && split.length != 0){
                for (int i = 0; i < split.length; i++){

                    String temp = split[i];
                    if(temp.length() == 1 || temp.length() == 2 || temp.length() == 3){
                        result ++;
                    }else {
                        int length = temp.length();
                        if(length % 3 == 0){
                            result = result + length / 3;
                        }else {
                            result = result + length / 3 + 1;
                        }
                    }
                }
            }

            System.out.println(result);
        }
    }
}

54、统计射击比赛成绩
给定一个射击比赛成绩单，包含多个选手若干次射击的成绩分数，请对每个选手按其最高3个分数之和进行降序排名，输出降序排名后的选手ID序列。条件如下：
1、一个选手可以有多个射击成绩的分数，且次序不固定。
2、如果一个选手成绩少于3个，则认为选手的所有成绩无效，排名忽略该选手。
3、如果选手的成绩之和相等，则成绩之和相等的选手按照其ID降序排列。

输入描述:
输入第一行，一个整数N，表示该场比赛总共进行了N次射击，产生N个成绩分数（2<=N<=100）。
输入第二行，一个长度为N整数序列，表示参与每次射击的选手ID（0<=ID<=99）。
输入第三行，一个长度为N整数序列，表示参与每次射击的选手对应的成绩（0<=成绩<=100）。
输出描述:
符合题设条件的降序排名后的选手ID序列。

示例1
输入
13
3,3,7,4,4,4,4,7,7,3,5,5,5
53,80,68,24,39,76,66,16,100,55,53,80,55
输出
5,3,7,4
说明
该场射击比赛进行了13次，参赛的选手为{3,4,5,7}。
3号选手成绩：53,80,55，最高3个成绩的和为：80+55+53=188。
4号选手成绩：24,39,76,66，最高3个成绩的和为：76+66+39=181。
5号选手成绩：53,80,55，最高3个成绩的和为：80+55+53=188。
7号选手成绩：68,16,100，最高3个成绩的和为：100+68+16=184。
比较各个选手最高3个成绩的和，有3号=5号>7号>4号，由于3号和5号成绩相等且ID号5>3，所以输出为：5,3,7,4

答案：
解法一：


import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Scanner;

public class Main
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		String a = in.nextLine();
		String b = in.nextLine();
		String[] bSplit = b.split(",");
		String c = in.nextLine();
		String[] cSplit = c.split(",");
		Map<Integer, Integer> countMap = new java.util.HashMap<>();
		Map<Integer, Integer> cjMap = new java.util.HashMap<>();
		Map<Integer, List<Integer>> cjDataMap = new java.util.HashMap<>();
		for (int i = 0; i < Integer.valueOf(a); i++)
		{
			Integer mc = Integer.valueOf(bSplit[i]);
			Integer cj = Integer.valueOf(cSplit[i]);
			if (countMap.containsKey(mc))
			{
				countMap.put(mc, countMap.get(mc) + 1);
				// cjMap.put(mc, cjMap.get(mc) + cj);
				List<Integer> data = cjDataMap.get(mc);
				insertList(data, cj);
				cjDataMap.put(mc, data);
			} else
			{
				List<Integer> data = new ArrayList<>();
				insertList(data, cj);
				countMap.put(mc, 1);
				// cjMap.put(mc, cj);
				cjDataMap.put(mc, data);
			}
		}
		for (Entry<Integer, List<Integer>> data : cjDataMap.entrySet())
		{
			if (data.getValue().size() < 3)
			{
				continue;
			}
			for (int i = 0; i < data.getValue().size(); i++)
			{
				if (i > 2)
				{
					break;
				}
				if (cjMap.containsKey(data.getKey()))
				{
					cjMap.put(data.getKey(), cjMap.g