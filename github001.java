package github;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class github001 {
	
	// �ڵ��� ��� 1267	
	public static void main(String[] args) throws IOException{
		
		int ys = 0;	// ���Ŀ����
		int ms = 0; // �ν� �����
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		 
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for(int i =0; i< n; i++) {
			int m = Integer.parseInt(st.nextToken());
			
			ys += ((m/30) + 1) * 10;
			ms += ((m/60) + 1) * 15;
		}
		
		if(ys > ms) {
			System.out.println("M " + ms);
		}else if(ms > ys) {
			System.out.println("Y " + ys);
		}else {
			System.out.println("Y M " + ys);
		}
	}

}
