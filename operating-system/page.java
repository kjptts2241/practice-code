import java.io.*;
import java.io.IOException;
import java.util.*;

/* Page 교체 알고리즘 */

public class page {
    public static void main(String[] args) throws IOException {

        File file = new File("page.inp"); // 파일 가져오기

        BufferedReader br = new BufferedReader(new FileReader(file)); // 파일 읽어오기
        BufferedWriter bw = new BufferedWriter(new FileWriter("page.out", true));

        List<String> list = new ArrayList<String>();
        String line;

        // 파일 내용 페이지 리스트에 담기
        while ((line = br.readLine()) != null) {
            list.add(line);
        }

        // 프로세스가 사용가능한 프레임의 개수
        int frameCnt =  Integer.parseInt(list.get(0));
        list.remove(0); // 첫째 줄 삭제

        // 페이지 폴트 계산 클래스 생성
        pageFaultClac FIFO_pfc = new pageFaultClac(list, frameCnt);
        pageFaultClac LRU_pfc = new pageFaultClac(list, frameCnt);
        pageFaultClac OPT_pfc = new pageFaultClac(list, frameCnt);

        // 각 알고리즘 페이지 폴트 계산
        FIFO_pfc.FIFO();
        LRU_pfc.LRU();
        OPT_pfc.OPT();

        // 출력
        bw.write("FIFO: " + FIFO_pfc.getPage_fault() + "\n");
        bw.write("LRU: " + LRU_pfc.getPage_fault() + "\n");
        bw.write("OPT: " + OPT_pfc.getPage_fault() + "\n");

        bw.flush();
        bw.close();
    }
}

class pageFaultClac{

    int page_fault; // 페이지 폴트 횟수

    List<String> list; // 요청 페이지 리스트
    int frameCnt; // 프레임 수

    public pageFaultClac(List<String> list, int frameCnt) {
        this.list = list;
        this.frameCnt = frameCnt;
    }

    public int getPage_fault() {
        return page_fault;
    }

    // FIFO 페이지 폴트 메소드
    public void FIFO() {

        Queue<String> q = new LinkedList<>(); // 큐 선언

        // 시작 페이지부터 마지막 페이지까지
        // 큐의 페이지들이랑 비교하면서 hit / 페이지 폴트
        for (int i = 0; i < list.size(); i++) {

            // 요청 페이지가 -1 이면 즉시 종료
            if (list.get(i).equals("-1")) break;

            Iterator iter = q.iterator();

            // 큐에 있는 페이지 개수가 프레임 개수 보다 작은 경우
            if (q.size() < frameCnt) {

                int isPage = 0; // 요청 페이지가 큐에 있다면 1 / 없다면 0

                // 요청 페이지가 큐에 있는지 비교하면서
                while(iter.hasNext()) {
                    if (list.get(i).equals(iter.next())) {
                        isPage = 1;
                        break; // 요청 페이지가 큐에 있다면 hit
                    }
                }

                // 요청 페이지가 큐에 없다면 큐에 페이지 추가
                if (isPage == 0) {
                    q.add(list.get(i));
                    page_fault += 1; // 페이지 폴트
                }

            } else { // 큐에 있는 페이지가 꽉 찼을 때

                int not_page = frameCnt; // 값이 0 이 되면 요청 페이지가 큐에 전부 없는 경우

                // 요청 페이지가 큐에 있는지 비교하면서
                while(iter.hasNext()) {
                    if (list.get(i).equals(iter.next())) break; // 요청 페이지가 큐에 있다면 hit
                    else not_page -= 1; // 큐에 없을 때마다 비교 횟수 줄이기
                }

                // 요청 페이지가 큐에 전부 없다면
                if (not_page == 0) {
                    q.remove(); // 가장 먼저 들어온 페이지를 dequeue
                    q.add(list.get(i)); // 요청 페이지 enqueue
                    page_fault += 1; // 페이지 폴트
                }
            }
        }
    }

    // LRU 페이지 폴트 메소드
    public void LRU() {


        ArrayList<String> frameList = new ArrayList<>();

        // 시작 페이지부터 마지막 페이지까지
        // 프레임 리스트의 페이지들이랑 비교하면서 hit / 페이지 폴트
        for (int i = 0; i < list.size(); i++) {

            // 요청 페이지가 -1 이면 즉시 종료
            if (list.get(i).equals("-1")) break;

            // 프레임 리스트에 있는 페이지 개수가 프레임 개수 보다 작은 경우
            if (frameList.size() < frameCnt) {

                // 요청 페이지가 프레임 리스트에 있다면
                if (frameList.contains(list.get(i))) {
                    frameList.remove(list.get(i)); // 해당 요청 페이지를 프레임 리스트에서 제거 후
                    frameList.add(list.get(i)); // 맨 뒤로 이동
                } else { // 없다면
                    frameList.add(list.get(i)); // 해당 요청 페이지를 맨 뒤에 추가
                    page_fault += 1; // 페이지 폴트
                }

            } else { // 프레임 리스트에 페이지가 꽉 찼을 때

                // 요청 페이지가 프레임 리스트에 있다면
                if (frameList.contains(list.get(i))) {
                    frameList.remove(list.get(i)); // 해당 요청 페이지를 프레임 리스트에서 제거 후
                    frameList.add(list.get(i)); // 맨 뒤로 이동
                } else { // 없다면
                    frameList.remove(0); // 프레임 리스트에서 맨 앞의 인덱스 값을 제거 후
                    frameList.add(list.get(i)); // 해당 요청 페이지를 맨 뒤에 추가
                    page_fault += 1; // 페이지 폴트
                }
            }
        }
    }

    // OPT 페이지 폴트 메소드
    public void OPT() {

        ArrayList<String> frameList = new ArrayList<>();

        // 시작 페이지부터 마지막 페이지까지
        // 프레임 리스트의 페이지들이랑 비교하면서 hit / 페이지 폴트
        for (int i = 0; i < list.size(); i++) {

            // 요청 페이지가 -1 이면 즉시 종료
            if (list.get(i).equals("-1")) break;

            // 프레임 리스트에 있는 페이지 개수가 프레임 개수 보다 작은 경우
            if (frameList.size() < frameCnt) {

                // 요청 페이지가 프레임 리스트에 있다면
                if (frameList.contains(list.get(i))) {} // 넘어가기
                else { // 없다면
                    frameList.add(list.get(i)); // 해당 요청 페이지를 맨 뒤에 추가
                    page_fault += 1; // 페이지 폴트
                }

            } else { // 프레임 리스트에 페이지가 꽉 찼을 때

                // 요청 페이지가 프레임 리스트에 있다면
                if (frameList.contains(list.get(i))) {} // 넘어가기
                else { // 없다면

                    String value = null; // 삭제 할 프레임 리스트의 값
                    int max = 0; // 요청 페이지의 예상 시간(간격)

                    // 예상 요청 페이지들과 프레임 리스트 값을 비교하면서
                    // 제일 늦게 쓰는 프레임 페이지나 요청 페이지들 중에 존재하지 않는 값을 삭제
                    for (String str : frameList) {

                        int isPage = 0; // 요청 페이지들 중에서의 존재 여부

                        for (int j = i; j < list.size(); j++) {
                            if (str.equals(list.get(j))) {
                                isPage = 1;
                                if (max < j) {
                                    max = j;
                                    value = str;
                                }
                                break;
                            }
                        }

                        // 요청 페이지들 중에 없다면 해당 프레임 값 저장
                        if (isPage == 0) {
                            value = str;
                            break;
                        }
                    }

                    frameList.remove(value); // 해당 프레임 페이지 삭제

                    frameList.add(list.get(i)); // 해당 요청 페이지를 맨 뒤에 추가
                    page_fault += 1; // 페이지 폴트
                }
            }
        }
    }
}


