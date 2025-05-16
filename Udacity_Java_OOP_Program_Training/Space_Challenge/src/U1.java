import java.util.Random;

public class U1 extends Rocket {
    public U1() {
        super(10000, 18000);  // น้ำหนักจรวด U1 = 10,000kg, น้ำหนักบรรทุกสูงสุด = 18,000kg
    }

    @Override
    public boolean launch() {
        double chanceOfExplosion = 0.05 * ((double) (currentWeight - rocketWeight) / (maxWeight - rocketWeight));
        return new Random().nextDouble() > chanceOfExplosion;
    }

    @Override
    public boolean land() {
        double chanceOfCrash = 0.01 * ((double) (currentWeight - rocketWeight) / (maxWeight - rocketWeight));
        return new Random().nextDouble() > chanceOfCrash;
    }
}
