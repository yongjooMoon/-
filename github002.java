package github;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class github002 {

	public static void main(String[] args) throws IOException{
		// �� �ּ� 1284
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		while(true) {
			String n = br.readLine();
			
			int length = 1;	// ȣ���� ����
			
			// 0�Է��̸� Ż��			
			if(n.equals("0")) {
				System.exit(0);
			}
			
			// ���ڿ� �迭�� ����
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
