package github;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class github003 {
	
	// ���� ��ȣ 2061	
	public static void main(String[] args) throws IOException{

		// ���Ѱ��� 1,000,000 ������ int�� Ŀ�� �Ұ����� BigInteger ���
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		BigInteger k = new BigInteger(st.nextToken());
		BigInteger l =  new BigInteger(st.nextToken());
		int num = 2;
		
		for(int i =2; i<l.intValue(); i++) {
			// k%num == 0 �̶� ����
			if(k.remainder(BigInteger.valueOf(num)).compareTo(BigInteger.ZERO) == 0) {
				break;
			}
			
			num++;
		}
		
		// num < l Ŭ��� ���� ��찡 �ƴϴ�
		if(l.compareTo(BigInteger.valueOf(num)) == 1) {
			System.out.println("BAD " + num);
		}else {
			System.out.println("GOOD");
		}
	}
}
