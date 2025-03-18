
public class DieRace {

	private int sides, points, pick;
	private String name;
	
	public DieRace() {
		
		sides = 6;
		points = 0;
		pick = ((int) Math.random()*sides) + 1; 
		name = "Player";
		
	}
	
	public DieRace(String n, int pck) {
		
		sides = 6;
		points = 0;
		pick = pck; 
		name = n;
		
	}
	
	public DieRace(int s, int poi, int pck, String n) {
		
		sides = s;
		points = poi;
		pick = pck; 
		name = n;

		
	}
	
	public int getPoints() {
		return points;
	}
	
	public String getName() {
		return name;
	}
	
	public int getPick() {
		return pick;
	}
	
	public void reset() {
		points = 0;
	}
	
	
	public void roll(){
		int land = (int) (Math.random()*sides) + 1;
		
		if (land == pick) {
			points ++;
			System.out.println(name + " got a point!");
		}
		
		else
			System.out.println(name + " landed on " + land);
				
		
	}

}
