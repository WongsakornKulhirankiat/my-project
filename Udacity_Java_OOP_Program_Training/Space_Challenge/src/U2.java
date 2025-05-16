import java.util.Random;

public class U2 extends Rocket {
    public U2() {
        super(18000, 29000);  // น้ำหนักจรวด U2 = 18,000kg, น้ำหนักบรรทุกสูงสุด = 29,000kg
    }

    @Override
    public boolean launch() {
        double chanceOfExplosion = 0.04 * ((double) (currentWeight - rocketWeight) / (maxWeight - rocketWeight));
        return new Random().nextDouble() > chanceOfExplosion;
    }

    @Override
    public boolean land() {
        double chanceOfCrash = 0.08 * ((double) (currentWeight - rocketWeight) / (maxWeight - rocketWeight));
        return new Random().nextDouble() > chanceOfCrash;
    }
}
