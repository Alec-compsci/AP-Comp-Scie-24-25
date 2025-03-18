
import java.util.Scanner; 

public class DiceRacer {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		System.out.println("Pick a number to land on");
		
		int pick = scan.nextInt();
		
		DieRace p1 = new DieRace("Player One", pick);
		DieRace p2 = new DieRace("Player Two", pick);
		
		boolean running = true;
		boolean overtime = false;
		
		
		for(int r=0;r<=1;r++) {
		
		running = true;
		overtime = false;
		p1.reset();
		p2.reset();
		System.out.println("===");
		System.out.print("THE GAME STARTS\n" + "<----------->\n");

		while (running) {
			
			
			p1.roll();
			p2.roll();
			
			if (p1.getPoints() == 5 && p2.getPoints() == 5) {
				overtime = true;
				System.out.println("Both players have gotten 5 points! It's overtime and first to get to 6 wins!");
			}
			
			else if (p1.getPoints() == 5 && !overtime) {
				System.out.println("GAME OVER\n" + p1.getName() + " wins!");
				running = false;
			}
		
			else if (p2.getPoints() == 5 && !overtime) {
				System.out.println("GAME OVER\n" + p2.getName() + " wins!");
				running = false;
			}
		
			else if (p1.getPoints() == 6 && overtime) {
				System.out.println("GAME OVER\n" + p1.getName() + " wins on overtime!");
				running = false;
			}
		
			else if (p2.getPoints() == 6 && overtime) {
				System.out.println("GAME OVER\n" + p2.getName() + " wins on overtime!");
				running = false;
			}
			
		}
		 }
		
	}

}
