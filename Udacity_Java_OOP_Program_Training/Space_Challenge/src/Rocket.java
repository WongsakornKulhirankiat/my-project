public class Rocket implements SpaceShip {
    int rocketWeight;
    int maxWeight;
    int currentWeight;

    public Rocket(int rocketWeight, int maxWeight) {
        this.rocketWeight = rocketWeight;
        this.maxWeight = maxWeight;
        this.currentWeight = rocketWeight; // เริ่มต้นน้ำหนักคือแค่น้ำหนักจรวดเอง
    }

    @Override
    public boolean launch() {
        return true;  // จะถูก override ใน U1 และ U2
    }

    @Override
    public boolean land() {
        return true;  // จะถูก override ใน U1 และ U2
    }

    @Override
    public boolean canCarry(Item item) {
        return currentWeight + item.getWeight() <= maxWeight;
    }

    @Override
    public void carry(Item item) {
        currentWeight += item.getWeight();
    }
}
