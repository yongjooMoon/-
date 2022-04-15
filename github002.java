package github;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class github002 {

	public static void main(String[] args) throws IOException{
		// 집 주소 1284
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		while(true) {
			String n = br.readLine();
			
			int length = 1;	// 호수판 길이
			
			// 0입력이면 탈출			
			if(n.equals("0")) {
				System.exit(0);
			}
			
			// 문자열 배열로 변경
			String[] arr = n.split("");
			
			
			for(int i=0; i<arr.length; i++) {
				if("1".equals(arr[i])) {
					length += 2;
				}else if("0".equals(arr[i])) {
					length += 4;
				}else {
					length += 3;
				}
				length++;
			}
			System.out.println(length);
		}

	}

}
