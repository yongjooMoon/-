package github;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class github003 {
	
	// 좋은 암호 2061	
	public static void main(String[] args) throws IOException{

		// 제한값이 1,000,000 까지라 int로 커버 불가능해 BigInteger 사용
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		BigInteger k = new BigInteger(st.nextToken());
		BigInteger l =  new BigInteger(st.nextToken());
		int num = 2;
		
		for(int i =2; i<l.intValue(); i++) {
			// k%num == 0 이랑 동일
			if(k.remainder(BigInteger.valueOf(num)).compareTo(BigInteger.ZERO) == 0) {
				break;
			}
			
			num++;
		}
		
		// num < l 클경우 좋은 경우가 아니다
		if(l.compareTo(BigInteger.valueOf(num)) == 1) {
			System.out.println("BAD " + num);
		}else {
			System.out.println("GOOD");
		}
	}
}
