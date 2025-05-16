import java.io.File;
import java.util.ArrayList;
import java.util.Scanner;

public class Simulation {

    public ArrayList<Item> loadItems(String fileName) throws Exception {
        ArrayList<Item> items = new ArrayList<>();
        File file = new File(fileName);
        Scanner scanner = new Scanner(file);

        while (scanner.hasNextLine()) {
            String[] line = scanner.nextLine().split("=");
            String name = line[0];
            int weight = Integer.parseInt(line[1]);
            items.add(new Item(name, weight));
        }

        scanner.close();
        return items;
    }

    public ArrayList<Rocket> loadU1(ArrayList<Item> items) {
        ArrayList<Rocket> rockets = new ArrayList<>();
        Rocket rocket = new U1();

        for (Item item : items) {
            if (!rocket.canCarry(item)) {
                rockets.add(rocket);
                rocket = new U1();  // เริ่มจรวดใหม่
            }
            rocket.carry(item);
        }
        rockets.add(rocket);  // อย่าลืมจรวดสุดท้าย

        return rockets;
    }

    public ArrayList<Rocket> loadU2(ArrayList<Item> items) {
        ArrayList<Rocket> rockets = new ArrayList<>();
        Rocket rocket = new U2();

        for (Item item : items) {
            if (!rocket.canCarry(item)) {
                rockets.add(rocket);
                rocket = new U2();  // เริ่มจรวดใหม่
            }
            rocket.carry(item);
        }
        rockets.add(rocket);  // อย่าลืมจรวดสุดท้าย

        return rockets;
    }

    public int runSimulation(ArrayList<Rocket> rockets) {
        int totalBudget = 0;

        for (Rocket rocket : rockets) {
            totalBudget += rocket instanceof U1 ? 100 : 120;  // ค่าใช้จ่ายจรวด U1 = 100 ล้าน, U2 = 120 ล้าน

            while (!rocket.launch() || !rocket.land()) {
                totalBudget += rocket instanceof U1 ? 100 : 120;  // ถ้าล้มเหลวต้องส่งใหม่
            }
        }

        return totalBudget;
    }
}
