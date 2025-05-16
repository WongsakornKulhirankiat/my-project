import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws Exception {
        Simulation simulation = new Simulation();

        // Phase 1
        ArrayList<Item> phase1Items = simulation.loadItems("src/Phase-1.txt");
        ArrayList<Rocket> u1RocketsPhase1 = simulation.loadU1(phase1Items);
        ArrayList<Rocket> u2RocketsPhase1 = simulation.loadU2(phase1Items);

        System.out.println("Phase 1 - U1 Rockets budget: $" + simulation.runSimulation(u1RocketsPhase1) + " Million");
        System.out.println("Phase 1 - U2 Rockets budget: $" + simulation.runSimulation(u2RocketsPhase1) + " Million");

        // Phase 2
        ArrayList<Item> phase2Items = simulation.loadItems("src/Phase-2.txt");
        ArrayList<Rocket> u1RocketsPhase2 = simulation.loadU1(phase2Items);
        ArrayList<Rocket> u2RocketsPhase2 = simulation.loadU2(phase2Items);

        System.out.println("Phase 2 - U1 Rockets budget: $" + simulation.runSimulation(u1RocketsPhase2) + " Million");
        System.out.println("Phase 2 - U2 Rockets budget: $" + simulation.runSimulation(u2RocketsPhase2) + " Million");
    }
}
