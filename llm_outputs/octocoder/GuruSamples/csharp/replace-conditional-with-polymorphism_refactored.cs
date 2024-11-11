public class Bird {
    //...
    public double getSpeed() {
        switch (type) {
            case EUROPEAN:
                return getBaseSpeed();
            case AFRICAN:
                return getBaseSpeed() - getLoadFactor() * numberOfCoconuts;
            case NORWEGIAN_BLUE:
                return isNailed? 0 : getBaseSpeed(voltage);
            default:
                throw new Exception("Should be unreachable");
        }
    }
}